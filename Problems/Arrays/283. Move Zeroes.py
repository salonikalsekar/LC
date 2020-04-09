class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0
        count = nums.count(0)

        while i < len(nums):
            if nums[i] == 0:
                if i == len(nums) - count:
                    return nums
                del nums[i]
                nums.append(0)
            else:
                i += 1

        return (nums)