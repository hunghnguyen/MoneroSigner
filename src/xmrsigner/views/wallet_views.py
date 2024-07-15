from xmrsigner.models.qr_type import QRType
from .view import NotYetImplementedView, View, Destination, BackStackView, MainMenuView
from xmrsigner.models.encode_qr import EncodeQR
from xmrsigner.gui.screens import seed_screens, WarningScreen
from xmrsigner.helpers.wallet import MoneroWalletRPCManager


class WalletViewKeyQRView(View):

    def __init__(self, seed_num: int):
        super().__init__()
        self.seed_num: int = seed_num
        self.wallet = self.controller.get_seed(seed_num).wallet
        self.height = self.controller.get_seed(seed_num).height
    

    def run(self):
        e = EncodeQR(
            wallet=self.wallet,
            qr_type=QRType.WALLET_VIEW_ONLY
        )
        data = e.next_part()

        ret = seed_screens.WalletViewKeyQRScreen(
            qr_data=data
        ).display()

        return Destination(BackStackView)


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
