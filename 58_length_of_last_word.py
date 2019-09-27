class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        print(s)
        s = s.split(" ")[-1]
        if s:
            return(len(s))
        else: return 0