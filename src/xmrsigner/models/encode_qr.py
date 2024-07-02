import math

from monero.wallet import Wallet

from binascii import b2a_base64, hexlify
from dataclasses import dataclass
from typing import List, Optional
from xmrsigner.helpers.ur2.ur_encoder import UREncoder
from xmrsigner.helpers.ur2.ur import UR
from xmrsigner.helpers.qr import QR
from xmrsigner.models.qr_type import QRType
from xmrsigner.models.seed import Seed
from xmrsigner.helpers.compactseed import CompactSeed

from urtypes.crypto import PSBT as UR_PSBT
from urtypes.crypto import PSBT  # TODO: 2024-06-14, used as quickfix to remove embit.psbt.PSBT! Adapt for monero
from urtypes.crypto import Account, HDKey, Output, Keypath, PathComponent, SCRIPT_EXPRESSION_TAG_MAP

from xmrsigner.models.settings import SettingsConstants



@dataclass
class EncodeQR:
    """
       Encode psbt for displaying as qr image
    """
    # TODO: Refactor so that this is a base class with implementation classes for each
    # QR type. No reason exterior code can't directly instantiate the encoder it needs.

    # Dataclass input vars on __init__()
    psbt: PSBT = None
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

        # PSBT formats
        if self.qr_type == QRType.PSBT__UR2:
            self.encoder = UrPsbtQrEncoder(psbt=self.psbt, qr_density=self.qr_density)

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
        elif self.qr_type == QRType.MONERO_ADDRESS:  # TODO: 2024-06-20, do we need that? For what purpose? Added with rebase from main to 0.7.0 from seedsigner
            self.encoder = MoneroAddressEncoder(address=self.monero_address)

        elif self.qr_type == QRType.SIGN_MESSAGE:
            self.encoder = SignedMessageEncoder(signed_message=self.signed_message)
        else:
            raise Exception('QR Type not supported')


    def total_parts(self) -> int:
        return self.encoder.seq_len()


    def next_part(self):
        return self.encoder.next_part()


    def part_to_image(self, part, width=240, height=240, border=3):
        return self.qr.qrimage_io(part, width, height, border)


    def next_part_image(self, width=240, height=240, border=3, background_color="bdbdbd"):
        part = self.next_part()
        if self.qr_type == QRType.SEED__SEEDQR:
            return self.qr.qrimage(part, width, height, border)
        else:
            return self.qr.qrimage_io(part, width, height, border, background_color=background_color)


    # TODO: Make these properties?
    def is_complete(self):
        return self.encoder.is_complete


    def get_qr_density(self):
        return self.qr_density


    def get_qr_type(self):
        return self.qr_type


class BaseQrEncoder:

    def seq_len(self):
        raise Exception("Not implemented in child class")

    def next_part(self) -> str:
        raise Exception("Not implemented in child class")

    @property
    def is_complete(self):
        raise Exception("Not implemented in child class")

    def _create_parts(self):
        raise Exception("Not implemented in child class")


class BaseStaticQrEncoder(BaseQrEncoder):

    def seq_len(self):
        return 1

    @property
    def is_complete(self):
        return True


class BasePsbtQrEncoder(BaseQrEncoder):

    def __init__(self, psbt: PSBT):
        self.psbt = psbt


class UrPsbtQrEncoder(BasePsbtQrEncoder):

    def __init__(self, psbt, qr_density):
        super().__init__(psbt)
        self.qr_max_fragment_size = 20
        
        qr_ur_bytes = UR('crypto-psbt', UR_PSBT(self.psbt.serialize()).to_cbor())

        if qr_density == SettingsConstants.DENSITY__LOW:
            self.qr_max_fragment_size = 10
        elif qr_density == SettingsConstants.DENSITY__MEDIUM:
            self.qr_max_fragment_size = 30
        elif qr_density == SettingsConstants.DENSITY__HIGH:
            self.qr_max_fragment_size = 120

        self.ur2_encode = UREncoder(ur=qr_ur_bytes, max_fragment_len=self.qr_max_fragment_size)

    def seq_len(self):
        return self.ur2_encode.fountain_encoder.seq_len()

    def next_part(self) -> str:
        return self.ur2_encode.next_part().upper()

    @property
    def is_complete(self):
        return self.ur2_encode.is_complete()


class SeedQrEncoder(BaseStaticQrEncoder):

    def __init__(self, seed_phrase: List[str], wordlist: List[str]):
        super().__init__()
        self.seed_phrase = seed_phrase
        self.wordlist = wordlist
        
        if self.wordlist == None:
            raise Exception('Wordlist Required')

    def next_part(self):
        data = ""
        # Output as Numeric data format
        for word in self.seed_phrase:
            index = self.wordlist.index(word)
            data += str("%04d" % index)
        return data


class CompactSeedQrEncoder(SeedQrEncoder):

    def next_part(self):
        seed_phrase = self.seed_phrase.copy()
        if len(seed_phrase) in (13, 25):  # monero seed with checksum word, remove checksum word at the end
            del seed_phrase[-1]

        if len(seed_phrase) not in (12, 16, 24):  # results in (17, 22, 33) bytes per seed
            raise Exception('Neither a monero seed nor a polyseed!')

        return CompactSeed(self.wordlist).bytes(seed_phrase)


class ViewOnlyWalletQrEncoder(BaseStaticQrEncoder):

    def __init__(self, wallet: Wallet, height: int = 0):
        super().__init__()
        self.wallet: Wallet = wallet
        self.height: int = height

    def next_part(self):
        return f'monero_wallet:{self.wallet.address()}?view_key={self.wallet.view_key()}&height={self.height}'

 
class MoneroAddressEncoder(BaseStaticQrEncoder):

    def __init__(self, address: str):
        super().__init__()
        self.address = address

    def next_part(self):
        return self.address


class SignedMessageEncoder(BaseStaticQrEncoder):
    """
    Assumes that a signed message will fit in a single-frame QR
    """ # TODO: 2024-06-20, I don't know yet, but I belief it will not be the case for Monero!
    def __init__(self, signed_message: str):
        super().__init__()
        self.signed_message = signed_message

    def next_part(self):
        return self.signed_message
