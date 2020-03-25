class Solution:
    def reverse(self, x: int) -> int:
        isNegative = 1
        if x < 0:
            isNegative = -1
            x = x * isNegative
        res = 0
        while x != 0:
            res = (res * 10) + (x % 10)
            x = x // 10

        if res < -2 ** 31 or res > (2 ** 31) - 1:
            return 0
        else:
            if isNegative < 0:
                return isNegative * res
            else:
                return res