from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = defaultdict(int)

        if len(s) == 0:
            return 0

        i = 0
        j = 0

        maxVal = 1

        while j < len(s):

            if s[j] in h:
                maxVal = max(maxVal, (j - i))
                i = max(i, h[s[j]] + 1)

            h[s[j]] = j
            j += 1

        maxVal = max(maxVal, (len(s) - i))

        return maxVal
