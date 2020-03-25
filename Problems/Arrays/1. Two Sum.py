from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = defaultdict(int)

        for idx, num in enumerate(nums):
            if target - num not in temp:
                temp[num] = idx
            else:
                return [temp[target - num], idx]
