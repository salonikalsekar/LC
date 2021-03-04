from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        temp = Counter(s)
        for k, v in temp.items():
            if v == 1:
                return s.index(k)

        return -1