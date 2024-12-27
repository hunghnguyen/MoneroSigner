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

def generate_mnemonic(language_code: str = 'en') -> List[str]:
    return MoneroSeed("", languages[language_code]).phrase.split()

def generate_mnemonic_from_bytes(entropy_bytes: bytes, language_code: str = 'en') -> List[str]:
    return MoneroSeed(hexlify(entropy_bytes).decode(), languages[language_code]).phrase.split()
