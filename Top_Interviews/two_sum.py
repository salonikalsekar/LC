from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = defaultdict(int)

        for idx, v in enumerate(nums):
            if target - v in h:
                return [idx, h[target - v]]
            else:
                h[v] = idx
