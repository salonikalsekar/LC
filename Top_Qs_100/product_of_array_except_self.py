class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0] * length

        answer[0] = 1

        for i in range(1, length):
            answer[i] = answer[i - 1] * nums[i - 1]

        R = 1

        for i in reversed(range(length)):
            answer[i] = R * answer[i]
            R *= nums[i]

        return answer
#         zeroExists = False
#         res = []
#         prod = 1
#         c = 0
#         for i in nums:
#             if i == 0:
#                 zeroExists = True
#                 c += 1
#             else:
#                 prod *= i

#         for i in nums:
#             if i != 0 and zeroExists:
#                 res.append(0)
#             else:
#                 if i == 0 and c > 1:
#                     res.append(i)
#                 elif i == 0 and c == 1:
#                     res.append(prod)
#                 else:
#                     res.append(prod // i)

#         return res