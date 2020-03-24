class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        end = ''
        seen = {}
        sign = ''

        if numerator * denominator < 0:
            sign = '-'

        quot, remainder = divmod(abs(numerator), abs(denominator))

        while remainder != 0:

            if remainder in seen:
                end = end[:seen[remainder]] + "(" + end[seen[remainder]:] + ")"
                break
            seen[remainder] = len(end)
            quot1, remainder = divmod(remainder * 10, abs(denominator))
            end += str(quot1)

        return sign + str(quot) + (end and '.' + end)



