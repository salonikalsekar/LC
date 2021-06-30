from collections import Counter


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = Counter(nums)
        h = c.keys()

        for i, k in enumerate(h):
            nums[i] = k

        return len(h)