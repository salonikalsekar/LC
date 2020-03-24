from collections import defaultdict


class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.minimum = 300
        self.hitdict = defaultdict(int)

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.hitdict[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        res = 0
        for i in range(timestamp, timestamp - self.minimum, -1):
            res += self.hitdict[i]

        return res

    # Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)