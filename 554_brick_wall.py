from collections import defaultdict


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:

        temp = defaultdict(int)

        for i in wall:
            key = 0
            for j in range(len(i) - 1):
                key += i[j]
                temp[key] += 1

        if temp:
            return (len(wall) - max(temp.values()))
        else:
            return len(wall)


