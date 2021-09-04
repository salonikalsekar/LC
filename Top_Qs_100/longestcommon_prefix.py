class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        start = 0
        end = len(strs) - 1

        i = 0
        r = ""
        strs = sorted(strs)

        while i < len(strs[0]) and i < len(strs[end]):
            if strs[start][i] != strs[end][i]:
                break
            else:
                r += strs[start][i]
                i += 1

        return r