from xmrsigner.models.qr_type import QRType
from xmrsigner.models.monero_encoder import MoneroKeyImageQrEncoder
from xmrsigner.views.view import NotYetImplementedView, View, Destination, BackStackView, MainMenuView
from xmrsigner.models.monero_encoder import ViewOnlyWalletQrEncoder, ViewOnlyWalletJsonQrEncoder
from xmrsigner.gui.screens import seed_screens, WarningScreen, ButtonListScreen
from xmrsigner.helpers.wallet import MoneroWalletRPCManager, WALLET_PORT
from xmrsigner.helpers.network import Network
from xmrsigner.helpers.monero import WalletRpcWrapper
from xmrsigner.models.settings_definition import SettingsConstants
from xmrsigner.gui.components import IconConstants, FontAwesomeIconConstants
from xmrsigner.gui.screens.screen import RET_CODE__BACK_BUTTON, QRDisplayScreen

from monero.wallet import Wallet as MoneroWallet
from monero.seed import Seed as MoneroSeed

from time import sleep
from typing import Union

class WalletViewKeyQRView(View):

    def __init__(self, seed_num: int):
        super().__init__()
        self.seed_num: int = seed_num
        self.wallet: MoneroWallet = self.controller.get_seed(seed_num).wallet
        self.height: int = self.controller.get_seed(seed_num).height

    def run(self):
        self.run_screen(
            QRDisplayScreen,
            qr_encoder=ViewOnlyWalletQrEncoder(self.wallet, self.height)
        )


class WalletViewKeyJsonQRView(WalletViewKeyQRView):

    def run(self):
        self.run_screen(
            QRDisplayScreen,
            qr_encoder=ViewOnlyWalletJsonQrEncoder(self.wallet, self.height)
        )


class WalletRpcView(View):
    """
    Get information about WalletRpc
    """

    def run(self):
        from xmrsigner.gui.screens.screen import WalletRpcScreen
        try:
            version = MoneroWalletRPCManager().get_version_string()
            if not version:
                raise Exception('Now wallet rpc found')
            self.run_screen(WalletRpcScreen, version=version)
        except Exception:
            self.run_screen(WarningScreen, title='Wallet RPC', text="Couldn't find Wallet RPC, without device is not working properly!", status_headline='Not found', status_color='red')
        from xmrsigner.views.settings_views import SettingsMenuView
        return Destination(SettingsMenuView)


class WalletMenuView(View):
    """
    Get information about WalletRpc
    """

    def run(self):
        from xmrsigner.gui.screens.screen import WalletRpcScreen
        try:
            open_wallets = []
            button_data = []
            daemons = self.controller.wallet_rpc_manager.get_all_daemon_statuses()
            for network, running in daemons.items():
                if running:
                    open_wallets.append(network)
            if len(open_wallets) == 0:
                self.run_screen(WarningScreen, title='No wallet open!', text='At the moment is no wallet open', status_headline='', status_color='red')
                return Destination(MainMenuView)
            for network in open_wallets:
                fp = self.controller.wallet_rpc_manager.get_fingerprint(network)
                print(f'{str(network)}: {fp}')
                if fp:
                    button_data.append((f'{str(network)}: {fp}', None, None, None, IconConstants.CHEVRON_RIGHT))
            selected_menu_num = self.run_screen(
                ButtonListScreen,
                title='Open Wallets',
                is_button_text_centered=False,
                button_data=button_data
            )
            if len(open_wallets) > 0 and selected_menu_num < len(open_wallets):
                return Destination(WalletOptionsView, view_args={'network': open_wallets[selected_menu_num]})
            if selected_menu_num == RET_CODE__BACK_BUTTON:
                return Destination(BackStackView)
        except Exception as e:
            raise e
            self.run_screen(WarningScreen, title='Wallet RPC', text="Couldn't find Wallet RPC, without device is not working properly!", status_headline='Not found', status_color='red')
        return Destination(MainMenuView)


class ExportKeyImagesView(View):

    def __init__(self, network: Union[str, Network]):
        super().__init__()
        self.network = Network.ensure(network)
        self.wallet: MoneroWallet = self.controller.get_wallet(self.network)

    def run(self):
        try:
            key_image = WalletRpcWrapper(self.wallet).get_encrypted_key_images()
        except Exception as e:
            print(e)
            raise e
            self.run_screen(WarningScreen, title='Key Images Export', text='Error on exporting key images from the wallet', status_headline='Failed!', status_color='red')
            return Destination(BackStackView)
        try:
            self.run_screen(
                QRDisplayScreen,
                qr_encoder=MoneroKeyImageQrEncoder(key_image, self.controller.settings.get_value(SettingsConstants.SETTING__QR_DENSITY))
            )
        except Exception as e:
            raise e
            self.run_screen(WarningScreen, title='Key Images Export', text='Error on exporting key images from the wallet', status_headline='Failed!', status_color='red')
            return Destination(BackStackView)
        return Destination(MainMenuView)


class WalletOptionsView(View):
    """
    Views for actions on individual seeds:
    """

    SCAN = ('Scan for Wallet', IconConstants.SCAN)
    EXPORT_KEY_IMAGES = ('Export Key Imags', IconConstants.QRCODE)
    VIEW_ONLY_WALLET = ('View only Wallet', IconConstants.QRCODE)
    PURGE_WALLET = ('Purge from Wallet', FontAwesomeIconConstants.TRASH_CAN, 'red', 'red')

    def __init__(self, network: Union[str, Network]):
        super().__init__()
        self.network = Network.ensure(network)
        self.fingerprint: str = self.controller.wallet_rpc_manager.get_fingerprint(self.network)

    def run(self):
        button_data = []
        button_data.append(self.SCAN)
        button_data.append(self.EXPORT_KEY_IMAGES)
        button_data.append(self.VIEW_ONLY_WALLET)
        button_data.append(self.PURGE_WALLET)
        selected_menu_num = self.run_screen(
            seed_screens.SeedOptionsScreen,  # TODO: 2024-07-23, create a WalletOptionsScreen!
            button_data=button_data,
            fingerprint=self.fingerprint,
            polyseed=False,
            my_monero=False,
            has_passphrase=False
        )

        if selected_menu_num == RET_CODE__BACK_BUTTON:
            return Destination(BackStackView)

        if button_data[selected_menu_num] == self.SCAN:
            from xmrsigner.views.scan_views import ScanUR2View
            return Destination(ScanUR2View)

        if button_data[selected_menu_num] == self.VIEW_ONLY_WALLET:  # TODO: 2024-06-10: finish implementation
            return Destination(WalletViewKeyQRView, view_args={'seed_num': self.seed_num})

        if button_data[selected_menu_num] == self.PURGE_WALLET:
            # return Destination(PurgeWalletView, view_args={'seed_num': self.seed_num})
            pass

        if button_data[selected_menu_num] == self.EXPORT_KEY_IMAGES:
            return Destination(ExportKeyImagesView, view_args={'network': self.network})


class LoadWalletView(View):

    def __init__(self, seed_num: int):
        super().__init__()

        self.loading_screen = None
        self.wallet_seed = self.controller.get_seed(seed_num)

        if self.controller.get_wallet(self.wallet_seed.network) is None or self.controller.get_wallet_seed(self.wallet_seed.network) != self.wallet_seed:
            # Run the loading screen while we wait. Can take up to 4 minutes
            from xmrsigner.gui.screens.screen import EtaLoadingScreenThread
            self.loading_screen = EtaLoadingScreenThread(text="Loading Wallet...", eta=180)
            self.loading_screen.start()

            try:
                # load wallet
                pass
                # sleep(120)
            except Exception as e:
                self.loading_screen.stop()
                raise e

    def run(self):
        if self.controller.get_wallet(self.wallet_seed.network) and self.controller.get_wallet_seed(self.wallet_seed.network) == self.wallet_seed:
            return Destination(BackStackView)
        try:
            network = self.wallet_seed.network
            self.controller.wallet_rpc_manager.start_daemon(network)
            print('Wait for rpc comming up...', end='', flush=True)
            while not self.controller.wallet_rpc_manager.is_rpc_running(network):
                print('.', end='', flush=True)
                sleep(0.2)
            print('Done')
            self.controller.wallet_rpc_manager.close_wallet(network)
            moneroSeed: MoneroSeed = self.wallet_seed.monero_seed
            self.controller.wallet_rpc_manager.load_wallet(
                network,
                self.wallet_seed.fingerprint,
                moneroSeed.public_address(),
                moneroSeed.secret_view_key(),
                moneroSeed.secret_spend_key(),
                self.wallet_seed.height,
                self.wallet_seed.passphrase
                )
            self.controller.set_wallet(network, MoneroWallet(port=WALLET_PORT.forNetwork(network)))
            self.controller.set_wallet_seed(network, self.wallet_seed)
        except Exception as e:
            # Error occured, we have no more progress
            if self.loading_screen:
                self.loading_screen.stop()
            raise e
        # Everything is set. Stop the loading screen
        if self.loading_screen:
            self.loading_screen.stop()
        return Destination(WalletMenuView)
