import math

from monero.wallet import Wallet

from binascii import b2a_base64, hexlify
from dataclasses import dataclass
from typing import List
from seedsigner.helpers.ur2.ur_encoder import UREncoder
from seedsigner.helpers.ur2.ur import UR
from seedsigner.helpers.qr import QR
from seedsigner.models import Seed, QRType

from urtypes.crypto import PSBT as UR_PSBT
from urtypes.crypto import PSBT  # TODO: 2024-06-14, used as quickfix to remove embit.psbt.PSBT! Adapt for monero
from urtypes.crypto import Account, HDKey, Output, Keypath, PathComponent, SCRIPT_EXPRESSION_TAG_MAP

from seedsigner.models.settings import SettingsConstants



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
    passphrase: str = None
    derivation: str = None
    network: str = SettingsConstants.MAINNET
    qr_type: str = None
    qr_density: str = SettingsConstants.DENSITY__MEDIUM
    wordlist_language_code: str = SettingsConstants.WORDLIST_LANGUAGE__ENGLISH

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
            self.encoder = SeedQrEncoder(seed_phrase=self.seed_phrase,
                                         wordlist_language_code=self.wordlist_language_code)

        elif self.qr_type == QRType.SEED__COMPACTSEEDQR:
            self.encoder = CompactSeedQrEncoder(seed_phrase=self.seed_phrase,
                                                wordlist_language_code=self.wordlist_language_code)

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


class SeedQrEncoder(BaseQrEncoder):

    def __init__(self, seed_phrase: List[str], wordlist_language_code: str):
        super().__init__()
        self.seed_phrase = seed_phrase
        self.wordlist = Seed.get_wordlist(wordlist_language_code)
        
        if self.wordlist == None:
            raise Exception('Wordlist Required')


    def seq_len(self):
        return 1


    def next_part(self):
        data = ""
        # Output as Numeric data format
        for word in self.seed_phrase:
            index = self.wordlist.index(word)
            data += str("%04d" % index)
        return data


    @property
    def is_complete(self):
        return True


class CompactSeedQrEncoder(SeedQrEncoder):

    def next_part(self):
        # Output as binary data format
        binary_str = ""
        for word in self.seed_phrase:
            index = self.wordlist.index(word)

            # Convert index to binary, strip out '0b' prefix; zero-pad to 11 bits
            binary_str += bin(index).split('b')[1].zfill(11)

        # We can exclude the checksum bits at the end
        if len(self.seed_phrase) == 24:
            # 8 checksum bits in a 24-word seed
            binary_str = binary_str[:-8]

        elif len(self.seed_phrase) == 12:
            # 4 checksum bits in a 12-word seed
            binary_str = binary_str[:-4]

        # Now convert to bytes, 8 bits at a time
        as_bytes = bytearray()
        for i in range(0, math.ceil(len(binary_str) / 8)):
            # int conversion reads byte data as a string prefixed with '0b'
            as_bytes.append(int('0b' + binary_str[i*8:(i+1)*8], 2))
        
        # Must return data as `bytes` for `qrcode` to properly recognize it as byte data
        return bytes(as_bytes)


class ViewOnlyWalletQrEncoder(BaseQrEncoder):

    def __init__(self, wallet: Wallet):
        super().__init__()
        self.wallet: Wallet = wallet

    def seq_len(self):
        return 1

    def next_part(self):
        return ''  # TODO: 2024-06-10, needs to return view only wallet URI


    @property
    def is_complete(self):
        return True
