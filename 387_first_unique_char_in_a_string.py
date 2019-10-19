# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         for i in s:
#             if s.count(i) == 1:
#                 return s.index(i)
#
#         return -1


# from collections import Counter


# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         d = Counter(s)
#
#         for k, v in d.items():
#             if v == 1:
#                 return s.index(k)
#
#         return -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = Counter(s)

        for i, ch in enumerate(s):
            if d[ch] == 1:
                return i

        return -1