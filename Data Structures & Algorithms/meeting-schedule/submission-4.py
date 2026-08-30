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

        (0, 30)
        (5, 10)
        (15, 20)
        

        sort by end time:
            two meetings conflict if
                prev_end > curr_start

        1   9   10  19  20  29  30  39  40  50
        a   b   a   b
        
        1   10
        9   20
        19  30
        29  40
        39  50
        '''

        intervals.sort(key=lambda x: x.start)

        for i in range(1, len(intervals)):
            prev = intervals[i - 1]
            curr = intervals[i]

            if prev.end > curr.start:
                return False
        
        return True
