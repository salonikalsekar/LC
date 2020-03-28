from collections import defaultdict


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        res = []
        scores = defaultdict(list)
        for i in items:
            scores[i[0]].append(i[1])
        for k, v in scores.items():
            c = 1
            avgVal = 0
            sumVal = 0
            for i in sorted(v, reverse=True):
                if c <= 5:
                    sumVal += i
                    c += 1
                else:
                    break

            avgVal = sumVal // 5
            res.append([k, avgVal])

        return res
