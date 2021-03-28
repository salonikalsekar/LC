class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        l = 0
        r = 0
        dictTemp = {}
        ans = []
        for i, c in enumerate(S):
            dictTemp[c] = i

        for idx, ch in enumerate(S):
            r = max(r, dictTemp[ch])
            if r == idx:
                ans.append(r - l + 1)
                l = idx + 1

        return ans