from collections import defaultdict


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        reachable = defaultdict(set)
        seen = set(stones)

        for i in stones:
            reachable[i] = set()

        reachable[1].add(1)

        for ip in stones[1:]:
            for step in reachable[ip]:
                for s in [step + ip, step + ip + 1, step + ip - 1]:
                    if s in reachable and s != ip:
                        reachable[s].add(s - ip)

        if reachable[stones[-1]]:
            return True



