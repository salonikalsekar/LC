# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         maxVal = nums[0]
#         for i in range(len(nums)):
#             ans = 0
#             for j in range(i,len(nums)):
#                 ans += nums[j]
#                 if ans > maxVal:
#                     maxVal = ans
#                 else:
#                     continue

#         return maxVal


# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         maxVal = nums[0]
#         ans = 0
#         temp = [maxVal]
#         for i in range(len(nums)):
#             print(nums[i])
#             print(min(temp))
#             ans += nums[i]
#             print("ans", ans)
#             temp.append(nums[i])
#             if ans >= min(temp):
#                 temp.append(ans)
#             else:
#                 print("else")
#                 ans = 0
#                 maxVal = 0


#         return(max(temp))