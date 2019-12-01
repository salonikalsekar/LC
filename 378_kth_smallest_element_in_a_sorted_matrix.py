from heapq import heappush, heappop


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        res = -1
        temp = []
        for i in range(len(matrix)):
            for j in matrix[i]:
                heappush(temp, j)

        for elem in range(k):
            res = heappop(temp)

        return (res)

        # res = []
#         for i in matrix:
#             res += i

#         return sorted(res)[k-1]