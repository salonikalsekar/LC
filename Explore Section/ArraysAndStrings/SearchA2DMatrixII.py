class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        i = 0
        j = len(matrix[0]) - 1

        while i <= len(matrix) - 1 and j >= 0:
            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:
                i += 1
            else:
                j -= 1

        return False