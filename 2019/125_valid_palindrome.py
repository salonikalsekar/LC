import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

        str1 = "".join(re.findall("[a-zA-Z0-9]", s)).lower()
        if len(str1) == 0:
            return True

        revStr = str1[::-1]
        if str1 == revStr:
            return True
        else:
            return False
