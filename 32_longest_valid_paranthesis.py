class Solution:
    def longestValidParentheses(self, s: str) -> int:

        r = 0
        l = 0

        llength = 0
        rlength = 0

        for i in s:

            if i == '(':
                l += 1

            else:
                r += 1

                if l == r:
                    llength = max(llength, r * 2)

                elif l < r:
                    l = 0
                    r = 0
        l = 0
        r = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "(":
                l += 1
                if l == r:
                    rlength = max(rlength, l * 2)

                elif l > r:
                    l = 0
                    r = 0
            else:
                r += 1

        return max(llength, rlength)