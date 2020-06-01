class Solution:
    def isPalindrome(self, s: str) -> bool:
        filteredS = filter(lambda c: c.isalnum(), s)
        lowerS = list(map(lambda c: c.lower(), filteredS))

        return list(lowerS) == lowerS[::-1]