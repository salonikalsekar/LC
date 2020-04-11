class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sumVal = 0
        prod = 1
        while n != 0:
            digit = n % 10
            sumVal += digit
            prod *= digit
            n = n // 10
        return prod - sumVal