class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums= sorted(nums)
        res = set()
        for i,n in enumerate(nums):
            t = -1 * n
            left = i+1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == t:
                    res.add((nums[left], nums[right], -t))
                    left += 1
                    right -= 1

                elif nums[left] + nums[right] < t:
                    left += 1

                elif nums[left] + nums[right] > t:
                    right -= 1
        return list(res)