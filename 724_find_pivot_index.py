class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        tot = sum(nums)
        leftSum = 0

        for i in range(len(nums)):
            if leftSum == (tot - leftSum - nums[i]):
                return i
            leftSum += nums[i]

        return -1