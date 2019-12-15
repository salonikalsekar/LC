class Solution:
    def longestPalindrome(self, s: str) -> str:

        start = 0
        end = 0

        for i in range(len(s)):
            left = self.expandCenter(i, i, s)
            right = self.expandCenter(i, i + 1, s)

            length = max(left, right)
            if length > (end - start):
                start = i - (length - 1) // 2
                end = i + length // 2

        return s[start:end + 1]

    def expandCenter(self, i, j, s):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1

        return j - i - 1




