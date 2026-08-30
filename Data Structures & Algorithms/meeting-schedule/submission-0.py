"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        '''
        0 5 10 15 20 25 30
        a b b  c  c     a

        (5, 10)
        (15, 20)
        (0, 30)

        sort by end time:
            two meetings conflict if
                prev_start > curr_start

        5 8
        9 15
        '''

        intervals.sort(key=lambda x: x.end)

        for i in range(len(intervals)):
            for j in range(i, len(intervals)):
                if intervals[i].start > intervals[j].start:
                    return False
        
        return True
