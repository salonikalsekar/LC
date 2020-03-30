from collections import Counter


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charsDict = Counter(chars)
        res = 0
        for i in words:
            temp = Counter(i)
            if not temp - charsDict:
                res += len(i)

        return res