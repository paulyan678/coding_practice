from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort intervals by their end times
        intervals.sort(key=lambda x: x[1])
        # Initialize variables
        end = intervals[0][1]
        count = 1  # Count of non-overlapping intervals

        for i in range(1, len(intervals)):
            # If the current interval does not overlap with the last added interval
            if intervals[i][0] >= end:
                count += 1
                end = intervals[i][1]  # Update the end to be the end of the current interval

        # The minimum number of intervals to remove is the total number - count of non-overlapping intervals
        return len(intervals) - count
