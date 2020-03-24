from collections import Counter


class Solution:
    def mostCommonWord(self, literatureText: str, wordsToExclude: List[str]) -> str:
        s = literatureText.lower()

        puncList = ['!', '?', "'", ',', ';', '.']
        for i in puncList:
            s = s.replace(i, " ")

        s1 = s.split()
        d = Counter(s1)
        for i in wordsToExclude:
            del d[i]
        maxValue = max(d.values())

        keyList = [k for k, v in d.items() if v == maxValue]
        res = []
        for i in keyList:
            if i not in wordsToExclude:
                res.append(i)

        return res[0]

