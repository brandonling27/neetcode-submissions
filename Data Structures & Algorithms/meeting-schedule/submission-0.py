"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort by start of each tuple
        # check each tuple -> if end of first tuple is greater than 
        # start of second tuple then we have a problem
        intervals.sort(key=lambda x:x.start)
        if len(intervals) <= 1:
            return True
        i = 1
        while (i < len(intervals)):
            end1 = (intervals[i - 1]).end
            start2 = (intervals[i]).start
            if start2 < end1:
                return False
            i+= 1
        return True