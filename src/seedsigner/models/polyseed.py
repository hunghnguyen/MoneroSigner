from .seed import Seed, InvalidSeedException

from binascii import hexlify
from polyseed.lang import Language
from polyseed.exceptions import PolyseedWordCountMissmatchException, PolyseedLanguageNotFoundException

class PolyseedSeed(Seed):
    def __init__(self,
                 mnemonic: List[str] = None,
                 passphrase: str = "",
                 wordlist_language_code: str = SettingsConstants.WORDLIST_LANGUAGE__ENGLISH) -> None:
        self.wordlist_language_code = wordlist_language_code
        self.prefered_language = wordlist_language_code

        if not mnemonic:
            raise Exception("Must initialize a Seed with a mnemonic List[str]")
        self._mnemonic: List[str] = unicodedata.normalize("NFKD", " ".join(mnemonic).strip()).split()

        self._passphrase: str = ''
        self.set_passphrase(passphrase, regenerate_seed=False)

        self.seed_bytes: bytes = None
        self._generate_seed()


    @staticmethod
    def get_wordlist(wordlist_language_code: str = SettingsConstants.WORDLIST_LANGUAGE__ENGLISH) -> List[str]:
        if wordlist_language_code == SettingsConstants.WORDLIST_LANGUAGE__ENGLISH:
            return Language.get_lang_by_code(wordlist_language_code).words
        else:
            try:
                return Language.get_lang_by_code(wordlist_language_code).words
            except PolyseedLanguageNotFoundException:
                pass
        raise Exception(f"Unrecognized wordlist_language_code {wordlist_language_code}")


    def _generate_seed(self) -> bool:
        try:
            ps: PolyseedSeed = None
            try:
                ps = PolyseedSeed.decode(self.mnemonic_str)
            except PolyseedWordCountMissmatchException:
                ps = PolyseedSeed .decode_explicit(self.mnemonic_str, self.prefered_language)
            if ps.is_encrypted():
                if not self.passphrase:
                    raise Exception('No passphrase provided for encrypted polyseed')
                ps.crypt(self.passphrase)
            self.seed_bytes = ps.keygen()
        except Exception as e:
            print(repr(e))
            raise InvalidSeedException(repr(e))
    
    def to_monero_seed(self, password: Optional[str]) -> Seed:
        Seed.from_key(hexlify(self.seed_bytes), password, self.wordlist_language_code)

    ### override operators    
    def __eq__(self, other: Seed):
        if isinstance(other, Seed):
            return self.seed_bytes == other.seed_bytes
        return False
