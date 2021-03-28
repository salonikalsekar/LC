class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True
            x = -1 * x

        n = int(str(x)[::-1])
        if -2 ** 31 >= n or n >= 2 ** 31 - 1:
            return 0

        if neg:
            n = -1 * n
        return n