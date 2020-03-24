class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:

        c = 0
        jset = set(J)

        for i in S:
            if i in jset:
                c += 1

        return c

