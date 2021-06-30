from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)

        h = sorted(c.items(), key=lambda x: x[1])
        for k, v in h:
            return k