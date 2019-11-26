from collections import defaultdict


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        count = 0
        d = defaultdict(list)

        for i in time:
            temp = i % 60
            temp1 = (60 - temp) % 60

            if temp1 in d:
                count += len(d[temp1])

            d[temp].append(i)

        return (count)