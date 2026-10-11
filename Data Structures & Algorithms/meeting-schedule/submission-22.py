"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for i in range(len(intervals)):
            for j in range(i+1, (len(intervals))):
                if intervals[j].start > intervals[i].start and intervals[j].start < intervals[i].end:
                    print("from 1")
                    return False
                if intervals[j].end > intervals[i].start and intervals[j].end < intervals[i].end:
                    print("from 2")
                    return False
                if intervals[j].start == intervals[i].start or intervals[j].end == intervals[i].end:
                    print(f"intervals[j].start: {intervals[j].start}")
                    print(f"intervals[i].start: {intervals[i].start}")
                    print(f"intervals[j].end: {intervals[j].end}")
                    print(f"intervals[i].end: {intervals[i].end}")
                    print("from 3")
                    return False
        return True