from hashlib import sha256
from typing import List

from monero.seed import wordlists
from monero.seed import Seed as MoneroSeed
from binascii import hexlify

languages = {
    'en': 'English',
    'zh_s': 'Chinese (simplified)',
    'nl': 'Dutch',
    'esperanto': 'Esperanto',
    'fr': 'French',
    'de': 'German',
    'it': 'Italian',
    'jp': 'Japanese',
    'lobjan': 'Lojban',
    'pt': 'Portuguese',
    'ru': 'Russian',
    'es': 'Spanish',
}


def generate_mnemonic_from_bytes(entropy_bytes: bytes, language_code: str = 'en') -> List[str]:
    return MoneroSeed(hexlify(entropy_bytes).decode(), languages[language_code]).phrase.split()

def generate_mnemonic_from_dice(roll_data: str) -> List[str]:
    entropy_bytes = sha256(roll_data.encode()).digest()

    if len(roll_data) == 50:
        # 12-word mnemonic; only use 128bits / 16 bytes
        entropy_bytes = entropy_bytes[:16]

    # Return as a list
    return generate_mnemonic_from_bytes(entropy_bytes)
