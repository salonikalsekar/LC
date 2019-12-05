class Solution:
    def canJump(self, nums: List[int]) -> bool:

        reach = 0

        for i, n in enumerate(nums):

            if i > reach:
                return False

            reach = max(reach, i + n)

            if reach >= len(nums) - 1:
                return True

# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         n= 0
#         res  = False

#         if nums[0] >= len(nums)-1:
#             return True

#         for i in range(1, nums[n]+1):
#             res = res or self.canJump(nums[i+n:])
#         return res
