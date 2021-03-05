class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s1 = [0 for i in range(0, len(s))]

        for i in range(0, len(s)):
            s1[indices[i]] = s[i]
        return ''.join(s1)