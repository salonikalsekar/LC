class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ''
        for i in s:
            if i.isalpha():
                x += i.lower()
            if i.isdigit():
                x += i

        return x[::] == x[::-1]