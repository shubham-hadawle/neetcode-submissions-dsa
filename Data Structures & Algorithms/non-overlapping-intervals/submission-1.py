class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals by start-time
        intervals = sorted(intervals, key = lambda x : x[0])

        prevEnd = intervals[0][1]
        result = 0

        for start, end in intervals[1:]:
            if start < prevEnd:
                result += 1
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end

        return result