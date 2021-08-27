from collections import defaultdict


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        res = defaultdict(int)
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                t = nums[l] + nums[r] + nums[i]
                if t == target:
                    return t

                elif t < target:
                    l += 1

                else:
                    r -= 1

                res[t] = abs(target - t)

        return min(res, key=res.get)

