class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        if not intervals:
            return 0

        total_rooms = 0

        start_times = sorted([i[0] for i in intervals])
        end_times = sorted([i[1] for i in intervals])

        L = len(intervals)

        start = 0
        end = 0

        while start < L:

            if start_times[start] >= end_times[end]:
                total_rooms -= 1
                end += 1

            total_rooms += 1
            start += 1

        return total_rooms


