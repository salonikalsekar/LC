# 7. Reverse Integer
# Easy

# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution:
    def reverse(self, x: int) -> int:
        i = x
        ans = 0
        if -2**31 <= x <= 2**31 -1:
            if x < 0:
                sign = -1 
                x = x * sign
            else :
                sign = 1
            while i != 0:
                ans = (x % 10) + (ans * 10)
                x = x // 10     
                i = x
            ans = sign * ans
            if -2**31 <= ans <= 2**31 -1:
                return ans
            else:
                return 0
        else:
            return 0
        
