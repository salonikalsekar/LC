class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        xset = set()
        yset = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    xset.add(i)
                    yset.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in xset or j in yset:
                    matrix[i][j] = 0

