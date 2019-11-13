from collections import defaultdict


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1

        judge = []
        seen = set()
        temp = defaultdict(list)

        for i in range(len(trust)):
            if trust[i][0] not in seen:
                seen.add(trust[i][0])
            if trust[i][1] not in seen:
                seen.add(trust[i][1])

            temp[trust[i][0]].append(trust[i][1])

        if len(temp) == N:
            return -1

        else:
            for i in seen:
                if i not in temp:
                    for v in temp.values():
                        if i not in v:
                            return -1
                    judge.append(i)

        if len(judge) == 1:
            return judge[0]
        else:
            return -1

