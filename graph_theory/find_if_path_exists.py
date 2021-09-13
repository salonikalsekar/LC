from collections import defaultdict

#dfs
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        s = []
        d = defaultdict(list)
        for i in edges:
            d[i[0]].append(i[1])
            d[i[1]].append(i[0])

        seen = set()
        s.append(start)

        while s:
            n = s.pop()
            if n == end:
                return True

            if n not in seen:
                seen.add(n)
                for i in d[n]:
                    s.append(i)

        return False



