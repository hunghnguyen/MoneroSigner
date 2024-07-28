from typing import List

from xmrsigner.controller import Controller

from xmrsigner.gui.components import GUIConstants
from xmrsigner.gui.components import FontAwesomeIconConstants, IconConstants
from xmrsigner.models.monero_encoder import MoneroSignedTxQrEncoder
from xmrsigner.helpers.monero import TxDescription, WalletRpcWrapper
from xmrsigner.models.tx_parser import TxParser
from xmrsigner.models.qr_type import QRType
from xmrsigner.models.settings import SettingsConstants
from xmrsigner.models.polyseed import PolyseedSeed
from xmrsigner.gui.screens.monero_screens import (
    TxOverviewScreen,
    TxMathScreen,
    TxAddressDetailsScreen,
    TxChangeDetailsScreen,
    TxFinalizeScreen
)
from xmrsigner.views.wallet_views import LoadWalletView
from xmrsigner.gui.screens.screen import (
    RET_CODE__BACK_BUTTON,
    ButtonListScreen,
    DireWarningScreen,
    LoadingScreenThread,
    QRDisplayScreen,
    WarningScreen
)
from xmrsigner.views.wallet_views import ImportOutputsView
from xmrsigner.views.view import (
    BackStackView,
    MainMenuView,
    NotYetImplementedView,
    View,
    Destination
)


class MoneroSelectSeedView(View):  # TODO: 2024-07-23, seems to me redundant code: @see xmrsigner.views.seed_views.SeedSelectSeedView

    SCAN_SEED = ("Scan a seed", FontAwesomeIconConstants.QRCODE)
    TYPE_13WORD = ("Enter 13-word seed", FontAwesomeIconConstants.KEYBOARD)
    TYPE_25WORD = ("Enter 25-word seed", FontAwesomeIconConstants.KEYBOARD)

    def __init__(self, flow: str):
        super().__init__()
        self.flow = flow

    def run(self):
        seeds = self.controller.storage.seeds

        button_data = []
        for seed in seeds:
            button_str = seed.fingerprint
            button_data.append((
                button_str,
                IconConstants.FINGERPRINT,
                GUIConstants.FINGERPRINT_POLYSEED_COLOR if isinstance(seed, PolyseedSeed) else GUIConstants.FINGERPRINT_MONERO_SEED_COLOR if not seed.is_my_monero else GUIConstants.FINGERPRINT_MY_MONERO_SEED_COLOR,
                None,
                FontAwesomeIconConstants.LOCK if seed.has_passphrase else None
            ))
        button_data.append(self.SCAN_SEED)
        button_data.append(self.TYPE_13WORD)
        button_data.append(self.TYPE_25WORD)

        selected_menu_num = self.run_screen(
            ButtonListScreen,
            title="Select Seed",
            is_button_text_centered=False,
            button_data=button_data
        )

        if selected_menu_num == RET_CODE__BACK_BUTTON:
            return Destination(BackStackView)

        if len(seeds) > 0 and selected_menu_num < len(seeds):
            # User selected one of the n seeds
            print(f'selected seed: {selected_menu_num}')
            self.controller.selected_seed = self.controller.get_seed(selected_menu_num)
            if self.flow == Controller.FLOW__SYNC:
                return Destination(ImportOutputsView)
            if self.flow == Controller.FLOW__TX:
                return Destination(OverviewView)
        
        # The remaining flows are a sub-flow; resume PSBT flow once the seed is loaded.
        # self.controller.resume_main_flow = Controller.FLOW__TX
        self.controller.resume_main_flow = self.flow

        if button_data[selected_menu_num] == self.SCAN_SEED:
            from xmrsigner.views.scan_views import ScanSeedQRView
            return Destination(ScanSeedQRView)

        elif button_data[selected_menu_num] in [self.TYPE_13WORD, self.TYPE_25WORD]:
            from xmrsigner.views.seed_views import SeedMnemonicEntryView
            if button_data[selected_menu_num] == self.TYPE_13WORD:
                self.controller.storage.init_pending_mnemonic(num_words=13)
            else:
                self.controller.storage.init_pending_mnemonic(num_words=25)
            return Destination(SeedMnemonicEntryView)


class OverviewView(View):

    def __init__(self):
        super().__init__()
        self.seed: Seed = self.controller.selected_seed
        self.wallet: MoneroWallet = self.controller.get_wallet(self.seed.network)

        self.loading_screen = None

        if not self.controller.tx_description:
            # Parsing could take a while. Run the loading screen while we wait.
            from xmrsigner.gui.screens.screen import LoadingScreenThread
            self.loading_screen = LoadingScreenThread(text="Parsing Transaction...")
            self.loading_screen.start()

    def run(self):
        print(f'wallet: {self.wallet}')
        print(f'seed: {self.seed}')
        print(f'controller has seed: {self.controller.has_seed(self.seed)}')
        if not self.wallet and self.seed and self.controller.has_seed(self.seed):
            print('No wallet, but seed and controller has seed')
            self.loading_screen.stop()
            return Destination(LoadWalletView, view_args={'seed_num': self.controller.get_seed_num(self.seed)})
        if self.controller.get_wallet_seed(self.seed.network) != self.seed:
            if self.loading_screen:
                self.loading_screen.stop()
                return Destination(LoadWalletView, view_args={'seed_num': self.controller.get_seed_num(self.seed)}) 
        try:
            txd: Optional[TxDescription] = WalletRpcWrapper(self.wallet).describe_transfer(self.controller.transaction)
            # Everything is set. Stop the loading screen
            if self.loading_screen:
                self.loading_screen.stop()
        except Exception as e:
            self.loading_screen.stop()
            raise e
        self.loading_screen.stop()
        if txd is None:
            selected_menu_num = WarningScreen(
                status_headline='No valid Transaction',
                text="This Transaction seems to be invalid.",
                button_data=["Continue"],
            ).display()
            return Destination(MainMenuView)
        self.controller.tx_description = txd
        # Run the overview screen
        selected_menu_num = self.run_screen(
            TxOverviewScreen,
            spend_amount=int(txd.amount_out),
            change_amount=int(txd.change_amount),
            fee_amount=int(txd.fee),
            num_inputs=txd.inputs,
            num_self_transfer_outputs=txd.outputs,
            num_change_outputs=txd.change_outputs,
            destination_addresses=[str(r.address) for r in txd.recipients]
        )
        if selected_menu_num == RET_CODE__BACK_BUTTON:
            self.controller.transaction = None
            self.controller.selected_seed = None
            return Destination(BackStackView)
        if txd.change_amount == 0:
            return Destination(NoChangeWarningView)
        return Destination(MathView)


class NoChangeWarningView(View):
    def run(self):
        selected_menu_num = WarningScreen(
            status_headline="Full Spend!",
            text="This Transaction spends its entire input value. No change is coming back to your wallet.",
            button_data=["Continue"],
        ).display()

        if selected_menu_num == RET_CODE__BACK_BUTTON:
            return Destination(BackStackView)

        # Only one exit point
        return Destination(
            MathView,
            skip_current_view=True,  # Prevent going BACK to WarningViews
        )


class MathView(View):
    """
        Follows the Overview pictogram. Shows:
        + total input value
        - recipients' value
        - fees
        -------------------
        + change value
    """
    def run(self):
        if not self.controller.transaction:
            # Should not be able to get here
            return Destination(MainMenuView)
        txd: TxDescription = self.controller.tx_description
        selected_menu_num = self.run_screen(
            TxMathScreen,
            input_amount=int(txd.amount_in),
            num_inputs=1,
            spend_amount=int(txd.amount_out),
            num_recipients=len(txd.recipients),
            fee_amount=int(txd.fee),
            change_amount=int(txd.change_amount),
        )
        if selected_menu_num == RET_CODE__BACK_BUTTON:
            return Destination(BackStackView)
        if len(txd.recipients) > 0:
            return Destination(TxAddressDetailsView, view_args={"address_num": 0})
        # This is a self-transfer
        return Destination(TxChangeDetailsView, view_args={"change_address_num": 0})


class TxAddressDetailsView(View):
    """
    Shows the recipient's address and amount they will receive
    """
    def __init__(self, address_num: int):
        super().__init__()
        self.address_num: int = address_num

    def run(self):
        if self.controller.tx_description is None:
            # Should not be able to get here
            raise Exception('Routing error')
        txd: TxDescription = self.controller.tx_description
        title = 'Will Send'
        if len(txd.recipients) > 1:
            title += f' (#{self.address_num + 1})'

        if self.address_num < len(txd.recipients) - 1:
            button_data = ['Next Recipient']
        else:
            button_data = ['Next']
        print(txd.recipients)
        print(f'self.address_num: {self.address_num}')
        print(txd.recipients[self.address_num])
        selected_menu_num = self.run_screen(
            TxAddressDetailsScreen,
            title=title,
            button_data=button_data,
            address=str(txd.recipients[self.address_num].address),
            amount=str(txd.recipients[self.address_num].amount),
        )
        
        if selected_menu_num == RET_CODE__BACK_BUTTON:
            return Destination(BackStackView)
        if self.address_num < len(txd.recipients) - 1:
            # Show the next receive addr
            return Destination(TxAddressDetailsView, view_args={"address_num": self.address_num + 1})
        if txd.change_amount > 0 and False:  # TODO: 2024-07-27, decide what to do about
            # Move on to display change
            return Destination(TxChangeDetailsView, view_args={"change_address_num": 0})
        # There's no change output to verify. Move on to sign the Tx.
        return Destination(FinalizeView)


class TxChangeDetailsView(View):

    NEXT = "Next"

    def __init__(self, change_address_num):
        super().__init__()
        self.change_address_num = change_address_num
        loading_screen: Optional[LoadingScreenThread] = None

    def run(self):
        if not self.controller.tx_description:
            # Should not be able to get here
            return Destination(MainMenuView)
        txd: TxDescription = self.controller.tx_description
        title = "Self-Transfer"
        try:
            if is_change_derivation_path:
                loading_screen_text = "Verifying Change..."
            else:
                loading_screen_text = "Verifying Self-Transfer..."
            self.loading_screen = LoadingScreenThread(text=loading_screen_text)
            self.loading_screen.start()
            network = self.settings.get_value(SettingsConstants.SETTING__NETWORKS)[0]  # TODO: 2024-06-26, solve multi network issue
            if txd.address == calc_address or True:  # TODO: 2024-07-27, decide to check or remove
                is_change_addr_verified = True
                button_data = [self.NEXT]
        finally:
            if self.loading_screen:
                self.loading_screen.stop()
        if is_change_addr_verified == False:
            return Destination(AddressVerificationFailedView, view_args=dict(is_change=is_change_derivation_path, is_multisig=tx_parser.is_multisig), clear_history=True)
        selected_menu_num = self.run_screen(
            TxChangeDetailsScreen,
            title=title,
            button_data=button_data,
            address=change_data.get("address"),
            amount=change_data.get("amount"),
            is_multisig=tx_parser.is_multisig,
            fingerprint=seed_fingerprint,
            derivation_path=derivation_path,
            is_change_derivation_path=is_change_derivation_path,
            derivation_path_addr_index=derivation_path_addr_index,
            is_change_addr_verified=is_change_addr_verified,
        )

        if selected_menu_num == RET_CODE__BACK_BUTTON:
            return Destination(BackStackView)

        elif button_data[selected_menu_num] == self.NEXT:
            if self.change_address_num < tx_parser.num_change_outputs - 1:
                return Destination(TxChangeDetailsView, view_args={"change_address_num": self.change_address_num + 1})
            else:
                # There's no more change to verify. Move on to sign the Tx.
                return Destination(FinalizeView)
            
        elif button_data[selected_menu_num] == self.VERIFY_MULTISIG:
            from xmrsigner.views.seed_views import LoadMultisigWalletDescriptorView
            self.controller.resume_main_flow = Controller.FLOW__TX
            return Destination(LoadMultisigWalletDescriptorView)
            


class AddressVerificationFailedView(View):

    def __init__(self, is_change: bool = True, is_multisig: bool = False):
        super().__init__()
        self.is_change = is_change
        self.is_multisig = is_multisig


    def run(self):
        if self.is_multisig:
            title = "Caution"
            text = f"""Transacions {"change" if self.is_change else "self-transfer"} address could not be verified with your multisig wallet descriptor."""
        else:
            title = "Suspicious Transaction"
            text = f"""Transactions {"change" if self.is_change else "self-transfer"} address could not be generated from your seed."""
        
        self.run_screen(
            DireWarningScreen,
            title=title,
            status_headline="Address Verification Failed",
            text=text,
            button_data=["Discard Transaction"],
            show_back_button=False,
        )
        # We're done with this Tx. Route back to MainMenuView which always
        #   clears all ephemeral data (except in-memory seeds).
        return Destination(MainMenuView, clear_history=True)



class FinalizeView(View):

    APPROVE_TX = "Approve Transaction"

    def run(self):
        if not self.controller.tx_description:
            # Should not be able to get here
            return Destination(MainMenuView)

        tx_description: TxDescription = self.controller.tx_description
        transaction: Transaction = self.controller.transaction
        selected_menu_num = self.run_screen(
            TxFinalizeScreen,
            button_data=[self.APPROVE_TX]
        )
        if selected_menu_num == RET_CODE__BACK_BUTTON:
            return Destination(BackStackView)
        return Destination(SignedQRDisplayView)


class SignedQRDisplayView(View):

    def __init__(self):
        super().__init__()
        self.seed: Seed = self.controller.selected_seed
        self.wallet: MoneroWallet = self.controller.get_wallet(self.seed.network)

        self.loading_screen = None

        if not self.controller.transaction:
            return Destination(MainMenuView)
        # Parsing could take a while. Run the loading screen while we wait.
        from xmrsigner.gui.screens.screen import LoadingScreenThread
        self.loading_screen = LoadingScreenThread(text=f"Sign Tx for seed {self.seed.fingerprint}...")
        self.loading_screen.start()
    
    def run(self):
        try:
            signed_tx: str = WalletRpcWrapper(self.wallet).sign_transfer(self.controller.transaction)
            if not signed_tx:
                raise Exception('No valid transaction')
            qr_encoder = MoneroSignedTxQrEncoder(
                signed_tx,
                self.settings.get_value(SettingsConstants.SETTING__QR_DENSITY)
            )
        except Exception as e:
            if self.loading_screen:
                self.loading_screen.stop()
            print(f'SignedQRDisplayView.run(): {e}')
            return Destination(SigningErrorView)
        if self.loading_screen:
            self.loading_screen.stop()
        self.run_screen(QRDisplayScreen, qr_encoder=qr_encoder)
        # We're done with this Tx. Route back to MainMenuView which always
        #   clears all ephemeral data (except in-memory seeds).
        return Destination(MainMenuView, clear_history=True)


class SigningErrorView(View):

    SELECT_DIFF_SEED = "Select Diff Seed"

    def run(self):
        if not self.controller.tx_description:
            # Should not be able to get here
            return Destination(MainMenuView)
        txd: TxDescription = self.controller.tx_description
        # Just a WarningScreen here; only use DireWarningScreen for true security risks.
        selected_menu_num = self.run_screen(
            WarningScreen,
            title="Transaction Error",
            status_icon_name=IconConstants.WARNING,
            status_headline="Signing Failed",
            text="Signing with this seed did not add a valid signature.",
            button_data=[self.SELECT_DIFF_SEED],
        )

        # TODO: 2024-07-27, code missing here!
        if selected_menu_num == 0:
            # clear seed selected for psbt signing since it did not add a valid signature
            self.controller.selected_seed = None
            return Destination(SelectSeedView, clear_history=True)

        if selected_menu_num == RET_CODE__BACK_BUTTON:
            return Destination(BackStackView)
