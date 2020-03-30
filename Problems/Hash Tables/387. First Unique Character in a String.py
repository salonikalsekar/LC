from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        temp = Counter(s)
        for idx, i in enumerate(s):
            if temp[i] == 1:
                return idx
        return -1