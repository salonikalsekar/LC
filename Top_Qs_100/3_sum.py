class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()
        for idx, i in enumerate(nums):

            x = idx + 1
            y = len(nums) - 1
            target = -1 * nums[idx]
            while x < y:
                if nums[x] + nums[y] == target:
                    res.add((nums[idx], nums[x], nums[y]))
                    x += 1
                    y -= 1

                elif nums[x] + nums[y] < target:
                    x += 1

                else:
                    y -= 1

        return list(res)