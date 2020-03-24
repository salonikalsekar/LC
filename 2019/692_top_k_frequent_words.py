from collections import defaultdict


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not words:
            return []
        res = []
        setTemp = set(words)
        dictTemp = defaultdict(list)

        for i in setTemp:
            c = words.count(i)
            dictTemp[c].append(i)

        for key, v in sorted(dictTemp.items(), reverse=True):
            if len(res) == k:
                return res

            elif len(res) < k:
                if len(v) > 1:
                    for i in sorted(v):
                        if len(res) < k:
                            res.append(i)

                else:
                    res.append(v[0])

        return res

