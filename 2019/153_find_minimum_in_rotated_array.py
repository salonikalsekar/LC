class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        n = len(nums) - 1

        r = n

        while l < r:

            mid = (l + r) // 2

            if mid < n and nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[r]:
                l = mid + 1

            else:
                if nums[mid] < nums[r]:
                    r = mid - 1
                else:
                    r = r - 1

        return nums[l]

