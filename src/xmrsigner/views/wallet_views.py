from xmrsigner.models.qr_type import QRType
from .view import NotYetImplementedView, View, Destination, BackStackView, MainMenuView
from xmrsigner.models.encode_qr import EncodeQR
from xmrsigner.gui.screens import seed_screens


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
