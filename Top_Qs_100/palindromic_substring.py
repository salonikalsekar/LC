class Solution:
    def countSubstrings(self, s: str) -> int:
        c = 0
        def expandAroundCenter(i, j, s):
            a = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
                a += 1


            return a

        for i in range(len(s)):
            c += expandAroundCenter(i, i, s) # 1 3
            c += expandAroundCenter(i, i+1, s) # 2 2

        return c

