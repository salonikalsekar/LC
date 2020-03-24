class Solution:
    def findMissingRanges(self, nums, lower, upper):
        ans = []

        prev = lower - 1

        for i in range(len(nums) + 1):

            if i < len(nums):
                curr = nums[i]
            else:
                curr = upper + 1

            if prev + 1 < curr:

                if prev + 1 < curr - 1:
                    ans.append(str(prev + 1) + "->" + str(curr - 1))
                else:
                    ans.append(str(prev + 1))

            prev = curr

        return ans