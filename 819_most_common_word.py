from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        s = paragraph.lower()

        puncList = ['!', '?', "'", ',', ';', '.']
        for i in puncList:
            s = s.replace(i, " ")

        s1 = s.split()
        d = Counter(s1)
        for i in banned:
            del d[i]
        maxValue = max(d.values())

        keyList = [k for k, v in d.items() if v == maxValue]
        res = []
        for i in keyList:
            if i not in banned:
                res.append(i)

        return res[0]

