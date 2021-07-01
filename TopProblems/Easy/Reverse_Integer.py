class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True
            x = -1 * x
        s = str(x)[::-1]
        val = int(s)
        if neg:
            val = -1 * val

        if val < -2 ** 31 or val > 2 ** 31 - 1:
            return 0

        return val
