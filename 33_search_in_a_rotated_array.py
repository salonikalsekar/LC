class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums) - 1
        l = 0
        r = n

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            elif target > nums[mid]:
                if nums[l] <= target and nums[l] > nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            elif target < nums[mid]:
                if nums[r] >= target and nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
