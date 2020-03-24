# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if len(s) != 0:

#             temp = []
#             for i in range(len(s)):
#                 stemp = set()
#                 count = 0
#                 for ch in range(i, len(s)):
#                     if s[ch] in stemp:
#                         count = 1
#                         stemp = set()
#                         stemp.add(s[ch])

#                     else:
#                         stemp.add(s[ch])
#                         count += 1
#                     temp.append(count)


#             return(max(temp))
#         else:
#             return 0


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        if not s:
            return 0
        maxVal = 1
        startIdx = 0
        for i, ch in enumerate(s):
            if ch not in d:
                d[ch] = i
            else:
                maxVal = max(maxVal, i - startIdx)
                startIdx = max(startIdx, d[ch] + 1)
                d[ch] = i
        maxVal = max(maxVal, len(s) - startIdx)
        return (maxVal)





