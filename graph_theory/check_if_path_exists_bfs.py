from collections import defaultdict

from collections import defaultdict


class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        q = []
        d = defaultdict(list)
        for i in edges:
            d[i[0]].append(i[1])
            d[i[1]].append(i[0])

        seen = set()
        q.append(start)

        while q:
            n = q.pop(0)
            if n == end:
                return True

            if n not in seen:
                seen.add(n)
                for i in d[n]:
                    q.append(i)

        return False