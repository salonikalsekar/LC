class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        w = r = 0
        b = len(nums) - 1

        while w <= b:

            if nums[w] == 0:
                nums[r], nums[w] = nums[w], nums[r]
                w += 1
                r += 1

            elif nums[w] == 2:
                nums[b], nums[w] = nums[w], nums[b]
                b -= 1

            else:
                w += 1
