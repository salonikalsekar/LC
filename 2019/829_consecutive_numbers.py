class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        count = 1

        for i in range(1, N):
            sumVal = i
            for j in range(i+1, N):
                sumVal+= j
                if sumVal == N:
                    count += 1
                elif sumVal > N:
                    break
        return(count)