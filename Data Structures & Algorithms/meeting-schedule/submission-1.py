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

        1 5
        1 3

        0 1 2 3 4 5
            a   a
          b       b
        1 3
        1 5

        5 8
        9 15
        '''

        intervals.sort(key=lambda x: x.end)

        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                if intervals[i].start >= intervals[j].start:
                    return False
        
        return True
