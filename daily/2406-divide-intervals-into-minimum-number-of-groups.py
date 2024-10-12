import heapq


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:

        # use a min-heap (priority queue) to track the earliest end time of the current groups

        # First, we sort the intervals by their start time.
        # This ensures that when processing each interval, we are always considering the earliest starting intervals first.
        intervals = sorted(intervals, key=lambda x: x[0])
        ending_times = []

        for start, end in intervals:
            # If the current interval's start time is greater than or equal to the earliest end time in the heap,
            # we can use the same group, so we pop the smallest end time
            if ending_times and start >= ending_times[0]:
                heapq.heappop(ending_times)
            heapq.heappush(ending_times, end)
        return len(ending_times)
