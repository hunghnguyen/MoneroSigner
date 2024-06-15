from xmrsigner.models.qr_type import QRType
from .view import NotYetImplementedView, View, Destination, BackStackView, MainMenuView
from xmrsigner.models.encode_qr import EncodeQR


class WalletViewKeyQRView(View):

    def __init__(self, seed_num: int):
        super().__init__()
        self.seed_num: int = seed_num
        self.wallet = self.controller.get_seed(seed_num).get_wallet()
    

    def run(self):
        e = EncodeQR(
            seed_phrase=self.seed.mnemonic_list,
            qr_type=QRType.WALLET_VIEW_ONLY
        )
        data = e.next_part()

        ret = seed_screens.WalletViewKeyQRScreen(
            qr_data=data,
            num_modules=self.num_modules,
        ).display()

        if ret == RET_CODE__BACK_BUTTON:
            return Destination(BackStackView)
        
        else:
            return Destination(
                SeedTranscribeSeedQRZoomedInView,
                view_args={
                    "seed_num": self.seed_num,
                    "seedqr_format": self.seedqr_format
                }
            )
