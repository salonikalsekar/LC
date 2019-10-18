class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        c = nums.count(0)
        while i < len(nums):
            if nums[i] == 0:
                if i == len(nums) - c:
                    return nums
                del nums[i]
                nums.append(0)
            else:
                i += 1

        return nums