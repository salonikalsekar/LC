class Solution:
    def isPalindrome(self, x: int) -> bool:
        sign = 1
        if x < 0:
            x = sign * x
            sign = sign * -1
        num = x
        rev = 0
        while x > 0:
            rev = rev * 10 + (x % 10)
            x = x // 10

        if rev == num:
            return True
        else:
            return False