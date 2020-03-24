class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals = sorted(intervals, key=lambda x: x[0])

        start = intervals[0]

        for i in range(1, len(intervals)):
            if start[1] > intervals[i][0]:
                return False
            start = intervals[i]

        return True