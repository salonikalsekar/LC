class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = w = 0
        b = len(nums) - 1

        while w <= b:
            if nums[w] == 0:
                nums[w], nums[r] = nums[r], nums[w]
                w += 1
                r += 1
            elif nums[w] == 2:
                nums[b], nums[w] = nums[w], nums[b]
                b -= 1
            else:
                w += 1

