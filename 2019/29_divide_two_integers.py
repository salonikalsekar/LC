class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        is_negative = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        total = divisor

        while total <= dividend:
            curr_quotient = 1
            while (total + total) <= dividend:
                total += total
                curr_quotient += curr_quotient

            dividend -= total
            total = divisor
            quotient += curr_quotient

        return min(2147483647, max(-quotient if is_negative else quotient, -2147483648))





