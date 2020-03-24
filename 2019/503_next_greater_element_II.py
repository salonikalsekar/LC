class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        stack = []
        res = [-1] * len(nums)
        if not nums:
            return

        for l in range(2):
            for j in range(len(nums) - 1, -1, -1):

                if not stack:
                    stack.append(nums[j])

                else:

                    while stack and stack[-1] <= nums[j]:
                        stack.pop()

                    if stack:
                        res[j] = stack[-1]

                    stack.append(nums[j])

        return res

#         res = []


#         for i in range(len(nums)):
#             found = False
#             for num in nums[i+1:]:
#                     if num > nums[i]:
#                         res.append(num)
#                         found = True
#                         break

#             if not found:
#                 for num in nums[:i]:
#                     if num > nums[i]:
#                         res.append(num)  
#                         found = True
#                         break

#             if not found:
#                 res.append(-1)

#         return(res)

