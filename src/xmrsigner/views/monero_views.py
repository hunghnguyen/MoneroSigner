from typing import List

from xmrsigner.controller import Controller

from xmrsigner.gui.components import FontAwesomeIconConstants, IconConstants
from xmrsigner.models.monero_encoder import MoneroSignedTxQrEncoder
from xmrsigner.models.tx_parser import TxParser
from xmrsigner.models.qr_type import QRType
from xmrsigner.models.settings import SettingsConstants
from xmrsigner.models.polyseed import PolyseedSeed
from xmrsigner.gui.screens.monero_screens import TxOverviewScreen
from xmrsigner.gui.screens.screen import (
    RET_CODE__BACK_BUTTON,
    ButtonListScreen,
    DireWarningScreen,
    LoadingScreenThread,
    QRDisplayScreen,
    WarningScreen
)
from xmrsigner.views.view import (
    BackStackView,
    MainMenuView,
    NotYetImplementedView,
    View,
    Destination
)


class PSBT:  # TODO: 2024-06-14, quick fix to remove embit.psbt.PSBT
    pass

class MoneroSelectSeedView(View):  # TODO: 2024-07-23, seems to me redundant code

    SCAN_SEED = ("Scan a seed", FontAwesomeIconConstants.QRCODE)
    TYPE_13WORD = ("Enter 13-word seed", FontAwesomeIconConstants.KEYBOARD)
    TYPE_25WORD = ("Enter 25-word seed", FontAwesomeIconConstants.KEYBOARD)

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
            self.controller.transaction_seed = self.controller.get_seed(selected_menu_num)  # TODO: 2024-07-23, add transaction_seed to control
            return Destination(OverviewView)
        
        # The remaining flows are a sub-flow; resume PSBT flow once the seed is loaded.
        self.controller.resume_main_flow = Controller.FLOW__TX

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

        self.loading_screen = None

        if not self.controller.tx_parser or self.controller.tx_parser.seed != self.controller.transaction_seed:
            # Parsing could take a while. Run the loading screen while we wait.
            from xmrsigner.gui.screens.screen import LoadingScreenThread
            self.loading_screen = LoadingScreenThread(text="Parsing Transaction...")
            self.loading_screen.start()

            try:
                # TODO: 2024-07-23, if we have to setup something to parse
                pass
            except Exception as e:
                self.loading_screen.stop()
                raise e


    def run(self):
        tx_parser = self.controller.tx_parser

        change_data = tx_parser.change_data
        """
            change_data = [
                {
                    'address': 'bc1q............', 
                    'amount': 397621401, 
                    'fingerprint': ['22bde1a9', '73c5da0a'], 
                    'derivation_path': ['m/48h/1h/0h/2h/1/0', 'm/48h/1h/0h/2h/1/0']
                }, {},
            ]
        """
        spend_amount = 0
        change_amount = 0
        fee_amount = 0
        num_inputs = 0
        num_change_outputs = 0
        num_self_transfer_outputs = 0
        destination_addresses = []

        # Everything is set. Stop the loading screen
        if self.loading_screen:
            self.loading_screen.stop()

        # Run the overview screen
        selected_menu_num = self.run_screen(
            TxOverviewScreen,
            spend_amount=spend_amount,
            change_amount=change_amount,
            fee_amount=fee_amount,
            num_inputs=num_inputs,
            num_self_transfer_outputs=num_self_transfer_outputs,
            num_change_outputs=num_change_outputs,
            destination_addresses=destination_addresses
        )
        if selected_menu_num == RET_CODE__BACK_BUTTON:
            # TODO: 2024-07-23, discard transaction
            # self.controller.psbt_seed = None
            return Destination(BackStackView)
        if change_amount == 0:
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
        if not self.controller.transaction:  # pseudo variable for now
            # Should not be able to get here
            return Destination(MainMenuView)

        input_amount = 0
        num_inputs = 0
        spend_amount = 0
        num_recipients = 0
        fee_amount = 0
        change_amount = 0
        destination_addresses = []
        
        selected_menu_num = self.run_screen(
            TxMathScreen,
            input_amount=input_amount,
            num_inputs=num_inputs,
            spend_amount=spend_amount,
            num_recipients=num_destinations,
            fee_amount=fee_amount,
            change_amount=change_amount,
        )
        if selected_menu_num == RET_CODE__BACK_BUTTON:
            return Destination(BackStackView)
        if len(destination_addresses) > 0:
            return Destination(TxAddressDetailsView, view_args={"address_num": 0})
        # This is a self-transfer
        return Destination(XMRChangeDetailsView, view_args={"change_address_num": 0})


class DirectionsDetailsView(View):
    """
        Shows the recipient's address and amount they will receive
    """
    def __init__(self, address_num):
        super().__init__()
        self.address_num = address_num


    def run(self):
        tx_parser: TxParser = self.controller.tx_parser

        if not tx_parser:
            # Should not be able to get here
            raise Exception("Routing error")

        title = "Will Send"
        if tx_parser.num_destinations > 1:
            title += f" (#{self.address_num + 1})"

        if self.address_num < tx_parser.num_destinations - 1:
            button_data = ["Next Recipient"]
        else:
            button_data = ["Next"]

        selected_menu_num = self.run_screen(
            TxAddressDetailsScreen,
            title=title,
            button_data=button_data,
            address=tx_parser.destination_addresses[self.address_num],
            amount=tx_parser.destination_amounts[self.address_num],
        )

        if selected_menu_num == RET_CODE__BACK_BUTTON:
            return Destination(BackStackView)
        if self.address_num < len(tx_parser.destination_addresses) - 1:
            # Show the next receive addr
            return Destination(TxAddressDetailsView, view_args={"address_num": self.address_num + 1})
        elif tx_parser.change_amount > 0:
            # Move on to display change
            return Destination(TxChangeDetailsView, view_args={"change_address_num": 0})
        else:
            # There's no change output to verify. Move on to sign the Tx.
            return Destination(FinalizeView)


class XMRChangeDetailsView(View):


    NEXT = "Next"
    VERIFY_MULTISIG = "Verify Multisig Change"

    def __init__(self, change_address_num):
        super().__init__()
        self.change_address_num = change_address_num


    def run(self):
        tx_parser: TxParser = self.controller.tx_parser

        if not tx_parser:
            # Should not be able to get here
            return Destination(MainMenuView)

        # Can we verify this change addr?
        change_data = tx_parser.get_change_data(change_num=self.change_address_num)
        """
            change_data:
            {
                'address': 'bc1q............', 
                'amount': 397621401, 
                'fingerprint': ['22bde1a9', '73c5da0a'], 
                'derivation_path': ['m/48h/1h/0h/2h/1/0', 'm/48h/1h/0h/2h/1/0']
            }
        """

        # Single-sig verification is easy. We expect to find a single fingerprint
        # and derivation path.
        seed_fingerprint = self.controller.psbt_seed.fingerprint

        if seed_fingerprint not in change_data.get("fingerprint"):
            # TODO:SEEDSIGNER: Something is wrong with this psbt(?). Reroute to warning?
            return Destination(NotYetImplementedView)

        i = change_data.get("fingerprint").index(seed_fingerprint)
        derivation_path = change_data.get("derivation_path")[i]

        # 'm/84h/1h/0h/1/0' would be a change addr while 'm/84h/1h/0h/0/0' is a self-receive
        is_change_derivation_path = int(derivation_path.split("/")[-2]) == 1
        derivation_path_addr_index = int(derivation_path.split("/")[-1])

        if is_change_derivation_path:
            title = "Your Change"
            self.VERIFY_MULTISIG = "Verify Multisig Change"
        else:
            title = "Self-Transfer"
            self.VERIFY_MULTISIG = "Verify Multisig Addr"
        # if tx_parser.num_change_outputs > 1:
        #     title += f" (#{self.change_address_num + 1})"

        is_change_addr_verified = False
        if tx_parser.is_multisig:
            # if the known-good multisig descriptor is already onboard:
            if self.controller.multisig_wallet_descriptor:
                is_change_addr_verified = tx_parser.verify_multisig_output(self.controller.multisig_wallet_descriptor, change_num=self.change_address_num)
                button_data = [self.NEXT]

            else:
                # Have the Screen offer to load in the multisig descriptor.            
                button_data = [self.VERIFY_MULTISIG, self.NEXT]

        else:
            # Single sig
            try:
                if is_change_derivation_path:
                    loading_screen_text = "Verifying Change..."
                else:
                    loading_screen_text = "Verifying Self-Transfer..."
                loading_screen = LoadingScreenThread(text=loading_screen_text)
                loading_screen.start()

                # convert change address to script pubkey to get script type
                # pubkey = script.address_to_scriptpubkey(change_data["address"])  # TODO: 2024-06-14, removed to get rid of embit.script
                script_type = pubkey.script_type()
                
                # extract derivation path to get wallet and change derivation
                change_path = '/'.join(derivation_path.split("/")[-2:])
                wallet_path = '/'.join(derivation_path.split("/")[:-2])
                
                xpub = self.controller.psbt_seed.get_xpub(
                    wallet_path=wallet_path,
                    network=self.settings.get_value(SettingsConstants.SETTING__NETWORKS)[0]  # TODO: 2024-06-26, solve multi network issue
                )
                
                # take script type and call script method to generate address from seed / derivation
                # xpub_key = xpub.derive(change_path).key
                network = self.settings.get_value(SettingsConstants.SETTING__NETWORKS)[0]  # TODO: 2024-06-26, solve multi network issue
                # scriptcall = getattr(script, script_type)  # TODO: 2024-06-14, removed to get rid of embit.script
                if script_type == "p2sh":
                    # single sig only so p2sh is always p2sh-p2wpkh
                    # calc_address = script.p2sh(script.p2wpkh(xpub_key)).address(  # TODO: 2024-06-14, removed to get rid of embit.script
                    #    network=NETWORKS[SettingsConstants.network_name(network)]
                    #)
                    pass
                else:
                    # single sig so this handles p2wpkh and p2wpkh (and p2tr in the future)
                    # calc_address = scriptcall(xpub_key).address(  # TODO: 2024-06-14, removed to get rid of embit.network.NETWORKS
                    #    network=NETWORKS[SettingsConstants.network_name(network)]
                    #)
                    pass

                if change_data["address"] == calc_address:
                    is_change_addr_verified = True
                    button_data = [self.NEXT]

            finally:
                loading_screen.stop()

        if is_change_addr_verified == False and (not tx_parser.is_multisig or self.controller.multisig_wallet_descriptor is not None):
            return Destination(AddressVerificationFailedView, view_args=dict(is_change=is_change_derivation_path, is_multisig=tx_parser.is_multisig), clear_history=True)

        selected_menu_num = self.run_screen(
            PSXMRhangeDetailsScreen,
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
                return Destination(XMRChangeDetailsView, view_args={"change_address_num": self.change_address_num + 1})
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
        tx_parser: TxParser = self.controller.tx_parser
        transaction: Transaction = self.controller.transaction

        if not tx_parser:
            # Should not be able to get here
            return Destination(MainMenuView)
        selected_menu_num = self.run_screen(
            TxFinalizeScreen,
            button_data=[self.APPROVE_Tx]
        )
        if selected_menu_num == RET_CODE__BACK_BUTTON:
            return Destination(BackStackView)
            # Sign Tx
            sig_cnt = TxParser.sig_count(transaction)
            transaction.sign_with(tx_parser.root)
            trimmed_psbt = TxParser.trim(transaction)

            if sig_cnt == TxParser.sig_count(trimmed_psbt):
                # Signing failed / didn't do anything
                return Destination(SigningErrorView)
            self.controller.transaction = trimmed_psbt
            return Destination(SignedQRDisplayView)


class SignedQRDisplayView(View):
    
    def run(self):
        signed_tx: str = ''  # TODO: the actual hex encoded signed transaction from rpc
        qr_encoder = MoneroSignedTxQrEncoder(
            signed_tx,
            self.settings.get_value(SettingsConstants.SETTING__QR_DENSITY)
        )
        self.run_screen(QRDisplayScreen, qr_encoder=qr_encoder)
 
        # We're done with this Tx. Route back to MainMenuView which always
        #   clears all ephemeral data (except in-memory seeds).
        return Destination(MainMenuView, clear_history=True)


class SigningErrorView(View):

    SELECT_DIFF_SEED = "Select Diff Seed"

    def run(self):
        tx_parser: TxParser = self.controller.tx_parser
        if not tx_parser:
            # Should not be able to get here
            return Destination(MainMenuView)

        # Just a WarningScreen here; only use DireWarningScreen for true security risks.
        selected_menu_num = self.run_screen(
            WarningScreen,
            title="Transaction Error",
            status_icon_name=IconConstants.WARNING,
            status_headline="Signing Failed",
            text="Signing with this seed did not add a valid signature.",
            button_data=[self.SELECT_DIFF_SEED],
        )

        if selected_menu_num == 0:
            # clear seed selected for psbt signing since it did not add a valid signature
            self.controller.psbt_seed = None
            return Destination(SelectSeedView, clear_history=True)

        if selected_menu_num == RET_CODE__BACK_BUTTON:
            return Destination(BackStackView)
