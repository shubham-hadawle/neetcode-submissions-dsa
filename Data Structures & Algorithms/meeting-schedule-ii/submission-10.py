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
        start.sort()
        end.sort()

        s, e = 0, 0
        rooms, maxRooms = 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                rooms += 1
                s += 1
            else:
                rooms -= 1
                e += 1
            maxRooms = max(maxRooms, rooms)

        return maxRooms