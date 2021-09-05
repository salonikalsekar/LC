class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = [0] * len(nums)
        maxVal = -float('inf')
        res[0] = nums[0]

        for i in range(1, len(nums)):
            res[i] = max(nums[i], res[i - 1] + nums[i])

        return max(res)