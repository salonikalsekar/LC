from collections import defaultdict


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        c = 0
        nums = sorted(nums)
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                t = nums[l] + nums[r] + nums[i]

                if t < target:
                    c += (r - l)

                    l += 1

                else:
                    r -= 1
        return c

