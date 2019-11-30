class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return

        def permutations(first=0):

            if first == len(nums):
                output.append(nums[:])

            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                permutations(first + 1)

                nums[first], nums[i] = nums[i], nums[first]

        output = []
        permutations()
        return output