from collections import Counter


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        c = Counter(nums)

        for k, v in sorted(c.items(), key=lambda i: i[1], reverse=True):
            return k
