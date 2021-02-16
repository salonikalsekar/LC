from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        maxVal  = 0
        temp = defaultdict(int)
        i= 0
        j = 0
        length = 0

        while i< len(s) and j < len(s):
            if s[j] in temp:
                if temp[s[j]] < i:
                    temp[s[j]] = j
                elif i <= temp[s[j]]:
                    i = temp[s[j]] + 1
                    temp[s[j]] = j
            else:
                temp[s[j]] = j
            j += 1
            length = (j - 1) - i + 1
            maxVal = max(maxVal, length)
        return maxVal
