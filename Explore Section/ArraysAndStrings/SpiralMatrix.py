class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        right = len(matrix[0]) - 1
        left = 0
        top = 0
        bottom = len(matrix) - 1

        if len(matrix) < 1:
            return []

        while left <= right and top <= bottom:
            l = left
            while l <= right:
                res.append(matrix[top][l])
                l += 1
            top += 1

            t = top
            while t <= bottom:
                res.append(matrix[t][right])
                t += 1
            right -= 1

            r = right
            while r >= left and top <= bottom:
                res.append(matrix[bottom][r])
                r -= 1
            bottom -= 1

            b = bottom
            while b >= top and left <= right:
                res.append(matrix[b][left])
                b -= 1
            left += 1
        return res

