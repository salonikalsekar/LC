class Solution:
    def reverse(self, x: int) -> int:
        neg = 1
        if x < 0:
            neg = -1
            x = x * neg
        s = str(x)[::-1]

        n = neg * int(s)

        if n < -2 ** 31 or n > 2 ** 31 - 1:
            return 0

        return neg * int(s)