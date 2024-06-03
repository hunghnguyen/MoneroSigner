from hashlib import sha256
from typing import List

from polyseed import seed_phrase_from_bytes

# TODO: expire 2024-06-10, I think should be moved/merged with mnemonic_generation somehow and somewhere else, think about it.

def generate_mnemonic_from_bytes(entropy_bytes: bytes) -> List[str]:
    return seed_phrase_from_bytes(entropy_bytes).split(' ')  # TODO: expire 2024-07-31, handle seed languages...

def generate_mnemonic_from_dice(roll_data: str) -> List[str]:
    entropy_bytes = sha256(roll_data.encode()).digest()
    return generate_mnemonic_from_bytes(entropy_bytes)
