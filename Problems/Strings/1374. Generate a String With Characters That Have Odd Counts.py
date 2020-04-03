class Solution:
    def generateTheString(self, n: int) -> str:
        if n == 0:
            return ''
        elif n % 2 != 0:
            return n * 'a'
        else:
            return ((n - 1) * 'a') + 'b'
