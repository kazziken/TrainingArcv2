'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
determine if a person could attend all meetings.

example:

Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation: 
(0,30), (5,10) and (0,30),(15,20) will conflict
'''
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def can_attend_meetings(intervals):

        end = 0
        #sort by start
        for interval in sorted(intervals, key=lambda x: x.start):
            # if overlapping (start is less than the last end then its overlapping)
            if interval.end < end or interval.start < end:
                return False
            #update end with next interval.end
            end = interval.end
        return True