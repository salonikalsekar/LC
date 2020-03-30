from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        temp = Counter(s)
        res = ""
        for k, v in sorted(temp.items(), key = lambda x:x[1], reverse = True):
            res += k * v
        return res