from monero.wallet import Wallet
from binascii import b2a_base64, hexlify
from dataclasses import dataclass
from typing import List, Optional
from xmrsigner.helpers.ur2.ur_encoder import UREncoder
from xmrsigner.helpers.ur2.ur import UR
from xmrsigner.helpers.qr import QR
from xmrsigner.models.qr_type import QRType
from xmrsigner.models.seed import Seed
from xmrsigner.models.base_encoder import BaseQrEncoder
from xmrsigner.models.seed_encoder import SeedQrEncoder, CompactSeedQrEncoder
from xmrsigner.urtypes.xmr import XmrKeyImage, XmrTxSigned
from xmrsigner.models.settings import SettingsConstants



@dataclass
class EncodeQR(BaseQrEncoder):
    # Dataclass input vars on __init__()
    seed_phrase: List[str] = None
    passphrase: Optional[str] = None
    derivation: str = None
    network: str = SettingsConstants.MAINNET
    wallet: Wallet = None
    height: int = 0
    qr_type: str = None
    qr_density: str = SettingsConstants.DENSITY__MEDIUM
    wordlist_language_code: str = SettingsConstants.WORDLIST_LANGUAGE__ENGLISH
    wordlist: List[str] = None

    def __post_init__(self):
        self.qr = QR()
        if not self.qr_type:
            raise Exception('qr_type is required')
        if self.qr_density == None:
            self.qr_density = SettingsConstants.DENSITY__MEDIUM
        self.encoder: BaseQrEncoder = None
        # UR formats
        if self.qr_type == QRType.UR2:
            # self.encoder = UrQrEncoder(ur_type, ur_payload, qr_density=self.qr_density)
            pass
        # SeedQR formats
        elif self.qr_type == QRType.SEED__SEEDQR:
            self.encoder = SeedQrEncoder(
                                seed_phrase=self.seed_phrase,
                                wordlist=self.wordlist
                            )
        elif self.qr_type == QRType.SEED__COMPACTSEEDQR:
            self.encoder = CompactSeedQrEncoder(
                                seed_phrase=self.seed_phrase,
                                wordlist=self.wordlist
                            )
        elif self.qr_type == QRType.WALLET_VIEW_ONLY:
            self.encoder = ViewOnlyWalletQrEncoder(
                                wallet=self.wallet,
                                height=self.height
                            )
        # Misc formats
        elif self.qr_type == QRType.MONERO_ADDRESS:
            self.encoder = MoneroAddressEncoder(address=self.monero_address)
        else:
            raise Exception('QR Type not supported')

    def total_parts(self) -> int:
        return self.encoder.seq_len()

    def next_part(self):
        return self.encoder.next_part()

    def next_part_image(self, width=240, height=240, border=3, background_color="bdbdbd"):
        part = self.next_part()
        if self.qr_type == QRType.SEED__SEEDQR:
            return self.qr.qrimage(part, width, height, border)
        else:
            return self.qr.qrimage_io(part, width, height, border, background_color=background_color)

    @property
    def is_complete(self):
        return self.encoder.is_complete

    def get_qr_density(self):
        return self.qr_density

    def get_qr_type(self):
        return self.qr_type
