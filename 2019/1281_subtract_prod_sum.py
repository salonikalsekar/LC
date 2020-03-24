class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sumAns = 0

        while n != 0:
            digit = n % 10
            n = n // 10

            prod *= digit
            sumAns += digit

        return prod - sumAns