from collections import Counter


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        res = []

        c = sorted(c.items(), reverse=True, key=lambda x: (x[1], -x[0]))
        for k in c:
            res += [k[0]] * k[1]

        return res[::-1]