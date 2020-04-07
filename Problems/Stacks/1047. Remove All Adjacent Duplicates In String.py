class Solution:
    def removeDuplicates(self, S: str) -> str:
        s = []

        for i in S:
            if s and s[-1] == i:
                s.pop()
            else:
                s.append(i)

        return ''.join(s)