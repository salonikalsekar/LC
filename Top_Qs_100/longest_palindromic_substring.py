class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0

        def expanAround(i, j, s):

            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1

            return j - i - 1

        for i in range(len(s)):
            l = expanAround(i, i, s)
            r = expanAround(i, i + 1, s)

            length = max(l, r)

            if length > (end - start):
                start = i - (length - 1) // 2
                end = i + length // 2

        return s[start:end + 1]
