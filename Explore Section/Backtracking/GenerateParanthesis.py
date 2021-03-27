class Solution(object):
    def generateParenthesis(self, N):

        res = []
        left = 0
        right = 0

        def genparanthesis(left=0, right=0, s=''):
            if len(s) == N * 2:
                res.append(s)
                return

            if left < N:
                genparanthesis(left + 1, right, s + '(')
            if right < left:
                genparanthesis(left, right + 1, s + ')')

        genparanthesis()
        return res