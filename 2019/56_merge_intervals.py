class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return

        res = []

        intervals = sorted(intervals, key=lambda x: x[0])

        start = intervals[0]

        for i in range(1, len(intervals)):

            if intervals[i][0] <= start[1]:
                start[1] = max(start[1], intervals[i][1])
            else:
                res.append(start)
                start = intervals[i]

        res.append(start)

        return res