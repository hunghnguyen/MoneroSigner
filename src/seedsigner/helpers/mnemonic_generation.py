# TODO: expire 2024-07-01 what to do about this file? Do we do the same thing?

from hashlib import sha256
from typing import List

from monero.seed import wordlists
from monero.seed import Seed as MoneroSeed
from binascii import hexlify


def generate_mnemonic_from_bytes(entropy_bytes: bytes) -> List[str]:
    return MoneroSeed(hexlify(entropy_bytes).decode()).phrase.split(' ')  # TODO: expire 2024-07-31, handle seed languages...

def generate_mnemonic_from_dice(roll_data: str) -> List[str]:
    entropy_bytes = sha256(roll_data.encode()).digest()

    if len(roll_data) == 50:
        # 12-word mnemonic; only use 128bits / 16 bytes
        entropy_bytes = entropy_bytes[:16]

    # Return as a list
    return generate_mnemonic_from_bytes(entropy_bytes)
