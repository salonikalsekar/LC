class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum =  0
        total = sum(nums)
        for i in range(0, len(nums)):
            if leftSum == total - leftSum - nums[i]:
                return i
            leftSum = leftSum + nums[i]
        return -1