class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        matrix = [[0 for i in range(n)] for j in range(n)]

        if n == 0:
            return

        r1, r2 = 0, n - 1
        c1, c2 = 0, n - 1
        num = 0

        while r1 <= r2 and c1 <= c2:
            for c in range(c1, c2 + 1):
                num += 1
                matrix[r1][c] = num

            for r in range(r1 + 1, r2 + 1):
                num += 1
                matrix[r][c2] = num

            if r1 < r2 and c1 < c2:
                for c in range(c2 - 1, c1, -1):
                    num += 1
                    matrix[r2][c] = num

                for r in range(r2, r1, -1):
                    num += 1
                    matrix[r][c1] = num

            r1 += 1
            r2 -= 1
            c1 += 1
            c2 -= 1

        return matrix




