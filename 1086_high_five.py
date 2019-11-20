from collections import defaultdict


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

        d = defaultdict(list)
        res = []
        for i in items:
            d[i[0]].append(i[1])

        for k, v in d.items():
            v = sorted(v, reverse=True)

            tot = sum(v[:5])

            avgVal = tot // 5

            res.append([k, avgVal])

        return res


