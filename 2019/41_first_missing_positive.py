class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) > 0:

            for i in range(len(nums) + 1):
                print(i)
                if i not in nums and i > 0:
                    return (i)
            return nums[-1] + 1
        else:
            return 1
