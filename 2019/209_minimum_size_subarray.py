import sys


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        minLength = sys.maxsize
        start = 0
        sumVal = 0

        for end in range(len(nums)):

            sumVal += nums[end]

            while sumVal >= s:
                minLength = min(minLength, end - start + 1)
                sumVal -= nums[start]
                start += 1

        if minLength == sys.maxsize:
            return 0
        return minLength
