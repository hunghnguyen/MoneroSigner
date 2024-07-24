from xmrsigner.models.base_encoder import BaseStaticQrEncoder
from xmrsigner.models.ur_encoder import UrQrEncoder
from xmrsigner.urtypes.xmr import (
    XmrTxSigned,
    XMR_TX_SIGNED,
    XmrKeyImage,
    XMR_KEY_IMAGE
)
from xmrsigner.models.qr_type import QRType
from monero.wallet import Wallet
from monero.address import Address
from typing import Union
from binascii import unhexlify


class MoneroAddressEncoder(BaseStaticQrEncoder):

    def __init__(self, address: Union[str, Address]):
        super().__init__()
        self.address: str = address if type(address) == str else str(address)

    def next_part(self):
        return f'monero:{self.address}'

    def get_qr_type(self):
        return QRType.MONERO_ADDRESS


class ViewOnlyWalletQrEncoder(BaseStaticQrEncoder):

    def __init__(self, wallet: Wallet, height: int = 0):
        super().__init__()
        self.wallet: Wallet = wallet
        self.height: int = height

    def next_part(self):
        return f'monero_wallet:{self.wallet.address()}?view_key={self.wallet.view_key()}&height={self.height}'
    def get_qr_type(self):
        return QRType.WALLET_VIEW_ONLY


class MoneroKeyImageQrEncoder(UrQrEncoder):

    def __init__(self, key_images_blob: str, qr_density: str):
        super().__init__(
            XMR_KEY_IMAGE.type,
            XmrKeyImage(unhexlify(key_images_blob)).to_cbor(),
            qr_density
        )

    def get_qr_type(self):
        return QRType.XMR_KEYIMAGE_UR


class MoneroSignedTxQrEncoder(UrQrEncoder):

    def __init__(self, signed_tx: str, qr_density: str):
        super().__init__(
            XMR_TX_SIGNED.type,
            XmrTxSigned(unhexlify(signed_tx)).to_cbor(),
            qr_density
        )

    def get_qr_type(self):
        return QRType.XMR_TX_SIGNED_UR
