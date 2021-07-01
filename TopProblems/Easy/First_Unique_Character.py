from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)

        for k, v in c.items():
            if v == 1:
                return s.find(k)

        return -1