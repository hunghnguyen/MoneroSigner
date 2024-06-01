import unicodedata

from monero.seed import Seed as MoneroSeed
from monero.seed import wordlists as MoneroWordlists
from typing import List, Optional, Union
from hashlib import sha256
from binascii import unhexlify

from seedsigner.models.settings import SettingsConstants



class InvalidSeedException(Exception):
    pass



class Seed:
    def __init__(self,
                 mnemonic: List[str] = None,
                 passphrase: Optional[str] = None,
                 wordlist_language_code: str = SettingsConstants.WORDLIST_LANGUAGE__ENGLISH) -> None:
        self.wordlist_language_code = wordlist_language_code

        if not mnemonic:
            raise Exception("Must initialize a Seed with a mnemonic List[str]")
        self._mnemonic: List[str] = unicodedata.normalize("NFKD", " ".join(mnemonic).strip()).split()

        self._passphrase: Optional[str] = None
        self.set_passphrase(passphrase, regenerate_seed=False)

        self.seed_bytes: bytes = None
        self._generate_seed()


    @staticmethod
    def get_wordlist(wordlist_language_code: str = SettingsConstants.WORDLIST_LANGUAGE__ENGLISH) -> List[str]:
        if wordlist_language_code == SettingsConstants.WORDLIST_LANGUAGE__ENGLISH:
            if wordlist_language_code in SettingsConstants.ALL_WORDLIST_LANGUAGE_ENGLISH__NAMES:
                return MoneroWordlists.get_wordlist(SettingsConstants.ALL_WORDLIST_LANGUAGE_ENGLISH__NAMES[wordlist_language_code]).word_list
        raise Exception(f"Unrecognized wordlist_language_code {wordlist_language_code}")


    def _generate_seed(self) -> None:
        if self.passphrase is not None:
            raise Exception('Passwords for monero seeds are not yet implemented')
        try:
            self.seed_bytes = unhexlify(MoneroSeed(self.mnemonic_str, SettingsConstants.ALL_WORDLIST_LANGUAGE_ENGLISH__NAMES[self.wordlist_language_code]).hex)
        except Exception as e:
            print(repr(e))
            raise InvalidSeedException(repr(e))


    @property
    def mnemonic_str(self) -> str:
        return " ".join(self._mnemonic)
    

    @property
    def mnemonic_list(self) -> List[str]:
        return self._mnemonic
    

    @property
    def mnemonic_display_str(self) -> str:
        return unicodedata.normalize("NFC", " ".join(self._mnemonic))
    

    @property
    def mnemonic_display_list(self) -> List[str]:
        return unicodedata.normalize("NFC", " ".join(self._mnemonic)).split()


    @property
    def passphrase(self) -> Optional[str]:
        return self._passphrase
        

    @property
    def passphrase_display(self):
        if not self._passphrase:
            return ''
        return unicodedata.normalize("NFC", self._passphrase)


    def set_passphrase(self, passphrase: Optional[str] = None, regenerate_seed: bool = True):
        if passphrase and passphrase != '':
            self._passphrase = unicodedata.normalize("NFKD", passphrase)
        else:
            self._passphrase = None

        if regenerate_seed:
            # Regenerate the internal seed since passphrase changes the result
            self._generate_seed()


    @property
    def wordlist(self) -> List[str]:
        return self.get_wordlist(self.wordlist_language_code)


    def set_wordlist_language_code(self, language_code: str) -> None:
        if language_code in SettingsConstants.ALL_WORDLIST_LANGUAGE_ENGLISH__NAMES:
            self.wordlist_language_code = language_code
            return
        raise Exception(f"Unrecognized wordlist_language_code {language_code}")

    def get_fingerprint(self, network: str = SettingsConstants.MAINNET) -> str:
        print(f'network: {type(network)}, seed_bytes: {type(self.seed_bytes)}')  # TODO: 2024-06-01 remove, debug only
        return sha256(network.encode() + self.seed_bytes).hexdigest()[-6:].upper()  # TODO: remove comment after 2024-06-04 is there a better way for a fingerprint, is it only used to display the seeds temporarily saved?
    
    @staticmethod
    def from_key(key: Union[str, bytes], password: Union[str, bytes, None] = None, language_code: str = SettingsConstants.WORDLIST_LANGUAGE__ENGLISH) -> 'Seed':
        if password is not None:
            raise Exception('Passwords for monero seeds are not yet implemented')
        if type(key) == bytes:
            key = key.decode()
        if wordlist_language_code in SettingsConstants.ALL_WORDLIST_LANGUAGE_ENGLISH__NAMES:
            phrase = MoneroSeed(key, wordlSettingsConstants.ALL_WORDLIST_LANGUAGE_ENGLISH__NAMES[wordlist_language_code])
            return Seed(phrase, password, language_code)
        raise Exception(f"Unrecognized wordlist_language_code {wordlist_language_code}")

    ### override operators
    def __eq__(self, other):
        if isinstance(other, Seed):
            return self.seed_bytes == other.seed_bytes
        return False
