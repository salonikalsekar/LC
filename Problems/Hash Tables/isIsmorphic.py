class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sh = {}
        th = {}
        for idx, i in enumerate(s):
            if i not in sh:
                sh[i] = [idx]
            else:
                sh[i].append(idx)
        for idx, i in enumerate(t):
            if i not in th:
                th[i] = [idx]
            else:
                th[i].append(idx)

        return sorted(th.values()) == sorted(sh.values())
