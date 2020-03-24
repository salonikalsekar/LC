class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        temp = []
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if A[i] + A[j] < K:
                    temp.append(A[j] + A[i])

        if len(temp) != 0:
            return max(temp)

        else:
            return -1