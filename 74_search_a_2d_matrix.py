class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        i = len(matrix) - 1
        j = 0

        while i >= 0 and j <= len(matrix[0]) - 1:
            print
            if matrix[i][j] == target:
                return True

            elif target < matrix[i][j]:
                i -= 1

            else:
                j += 1

        return False