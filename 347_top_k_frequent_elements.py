# from collections import defaultdict

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:

#         res = []
#         dicttemp = defaultdict(list)
#         settemp = set(nums)

#         for i in settemp:
#             c = nums.count(i)
#             dicttemp[c].append(i)

#         for key,v in sorted(dicttemp.items(), reverse=True):
#             if len(res) == k:
#                 return res

#             if len(res) < k:
#                 if len(v) > 1:
#                     for i in v:
#                         if len(res) < k:
#                             res.append(i)
#                 else:
#                     res.append(v[0])

#         return res

from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c_dict = Counter(nums)

        return sorted(c_dict.keys(), key=c_dict.get, reverse=True)[:k]