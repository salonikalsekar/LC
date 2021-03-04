from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        if not s:
            return ''
        c = Counter(s)
        res = ''
        for k, v in sorted(c.items(), key=lambda x: x[1], reverse=True):
            res += k * v

        return res
