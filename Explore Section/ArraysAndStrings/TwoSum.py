class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for idx, i in enumerate(nums):
            if target - i in temp:
                return [temp[target - i], idx]
            else:
                temp[i] = idx

