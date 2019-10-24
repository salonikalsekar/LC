class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums = sorted(nums)
        for i in range(len(nums)):
            target = -1 * nums[i]

            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] == target:
                    ans.add((nums[right], nums[left], nums[i]))
                    left += 1
                    right -= 1

                elif nums[left] + nums[right] > target:
                    right -= 1

                else:
                    left += 1

        return list(ans)