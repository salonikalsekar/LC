class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not len(s.split()):
            return 0

        return len(s.split()[-1])