class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxStr = ''

        def checkPalindrome(l, r):
            left = -1
            right = -1
            while l >= 0 and r <= len(s) - 1:
                if s[l] == s[r]:
                    left = l
                    right = r
                    l -= 1
                    r += 1
                else:
                    break
            if left == -1 and right == -1:
                return ''
            return s[left:right + 1]

        for i in range(0, len(s)):
            oddStr = checkPalindrome(i, i)
            evenStr = checkPalindrome(i, i + 1)
            strTemp = ''
            if len(oddStr) > len(evenStr):
                strTemp = oddStr
            else:
                strTemp = evenStr
            if len(maxStr) < len(strTemp):
                maxStr = strTemp
        return maxStr

