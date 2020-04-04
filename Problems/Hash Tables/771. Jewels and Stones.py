from collections import Counter


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        SDict = Counter(S)
        c = 0
        for i in J:
            if i in SDict:
                c += SDict[i]

        return c