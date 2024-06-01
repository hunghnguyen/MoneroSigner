# TODO: what to do about this file? Do we do the same thing?

from hashlib import sha256
from typing import List

from monero.seed import wordlists
from monero.seed import Seed as MoneroSeed
from binascii import hexlify


def calculate_checksum(mnemonic: List[str], wordlist_language_code: str) -> List[str]:
    """
        Provide 13- or 25-word mnemonic, returns complete mnemonic w/checksum as a list.

        If 12- or 24-words are provided, append word `0000` to end of list as temp final
        word.
    """
    if len(mnemonic) not in (12, 13, 24, 25):
        raise Exception('invalid count of seed words in seed phrase')
    return mnemonic + [ wordlists.English.get_checksum(' '.join(mnemonic)) ]

def generate_mnemonic_from_bytes(entropy_bytes: bytes) -> List[str]:
    return MoneroSeed(hexlify(entropy_bytes).decode()).phrase.split(' ')  # TODO: expire 2024-07-31, handle seed languages...

def generate_mnemonic_from_dice(roll_data: str) -> List[str]:
    entropy_bytes = sha256(roll_data.encode()).digest()

    if len(roll_data) == 50:
        # 12-word mnemonic; only use 128bits / 16 bytes
        entropy_bytes = entropy_bytes[:16]

    # Return as a list
    return generate_mnemonic_from_bytes(entropy_bytes)



# TODO: expire 2014-06-30, so why then not remove, double check if still used somehow, if not, remove function
# Note: This currently isn't being used since we're now chaining hashed bytes for the
#   image-based entropy and aren't just ingesting a single image.
def generate_mnemonic_from_image(image) -> List[str]:
    hash = sha256(image.tobytes())
    return generate_mnemonic_from_bytes(hash.digest())
