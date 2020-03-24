# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         l = []
#         s = set()
#         for n in nums:
#             if n not in s:
#                 l.append(n)
#                 s.add(n)
#
#         nums[:len(s)] = l
#
#         return len(s)

    from collections import OrderedDict
    class Solution:
        def removeDuplicates(self, nums: List[int]) -> int:
            temp = OrderedDict()

            for x in nums:
                if x not in temp:
                    temp[x] = 1
                else:
                    temp[x] = + 1

            for i, k in enumerate(temp.keys()):
                nums[i] = k

            return len(temp)

    #         if not nums:
    #             return 0
    #         seen = set()
    #         nums[:] = [x for x in nums if x not in seen and not seen.add(x)]

    #         return(len(nums))
