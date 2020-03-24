class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []
        for interval in intervals:

            if interval[0] <= newInterval[1] and interval[1] >= newInterval[0]:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]

            else:
                res.append(interval)

        res.append(newInterval)

        res.sort(key=lambda x: x[0])
        return (res)

