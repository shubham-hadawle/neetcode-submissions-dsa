"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start, end = [], []

        for i in intervals:
            start.append(i.start)
            end.append(i.end)

        start, end = sorted(start), sorted(end)
        s, e = 0, 0     # Start-Pointer & End-Pointer
        result, count = 0, 0

        while s < len(start):
            if start[s] < end[e]:
                count += 1      # Meeting room required
                s += 1
            else:
                count -= 1      # Meeting room freed
                e += 1
            result = max(result, count)

        return result