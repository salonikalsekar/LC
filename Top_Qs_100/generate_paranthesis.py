class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def genParanthesis(n, s, left=0, right=0):

            if len(s) == n * 2:
                res.append(s)
                return

            if left < n:
                genParanthesis(n, s + '(', left + 1, right)
            if right < left:
                genParanthesis(n, s + ')', left, right + 1)

            return

        genParanthesis(n, '')
        return res
