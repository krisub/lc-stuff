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

        1   9   10  19  20  29  30  39  40  50
        a   b   a   b
        
        1   10
        9   20
        19  30
        29  40
        39  50

        0 8
        8 10
        '''

        intervals.sort(key=lambda x: x.end)

        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                if intervals[i].start >= intervals[j].start:
                    return False
                if intervals[j].start < intervals[i].end:
                    return False
        
        return True
