from typing import List


class ShortSeed:

    def __init__(self, wordlist: List[str], letters: int = 4):
        self.wordlist: List[str] = wordlist
        self.letters: int = letters
        self.shortlist: List[str] = [word[:self.letters] for word in self.wordlist]

    def expand(self, shortlist: List[str]) -> List[str]:
        return [self.wordlist[self.shortlist.index(word[:self.letters])] for word in shortlist]

    def reduce(self, completelist: List[str]) -> List[str]:
        return [word[:self.letters] for word in completelist]

    def test(self, completelist: List[str]) -> bool:
        return self.expand(self.reduce(completelist)) == completelist
