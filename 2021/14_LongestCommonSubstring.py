class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        s = strs[0]

        for i in range(1, len(strs)):
            s1 = strs[i]
            x = 0
            while True:
                if x == len(s1) or x == len(s):
                    s = s[:x]
                    break
                if s[x] == s1[x]:
                    x += 1
                else:
                    s = s[:x]
                    break
        return s