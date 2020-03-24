class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        maxVal = 0

        if not matrix:
            return 0

        dp = [[0 for i in range(len(matrix[0]) + 1)] for j in range(len(matrix) + 1)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if matrix[i][j] == '1':
                    dp[i + 1][j + 1] = min(min(dp[i][j + 1], dp[i + 1][j]), dp[i][j]) + 1
                    maxVal = max(maxVal, dp[i + 1][j + 1])

        return maxVal * maxVal


