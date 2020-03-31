class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s1 = sorted(s)
        t1 = sorted(t)
        for idx, i in enumerate(s1):
            if i != t1[idx]:
                return t1[idx]

        return t1[-1]