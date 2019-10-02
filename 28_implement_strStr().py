class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0 and len(haystack) == 0:
            return 0
        elif len(needle) == 0:
            return 0
        if needle in haystack and len(haystack) != 0:
            return haystack.index(needle)
        else:
            return -1
