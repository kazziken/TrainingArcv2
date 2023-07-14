'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
find the minimum number of conference rooms required.)

Example:
Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)
'''

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals):
        
        start = sorted([i[0] for i in intervals])
        end = sorted(i[1] for i in intervals)

        s = e = 0
        used_rooms, res = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                # A new meeting is starting
                used_rooms += 1
                s += 1
            else:
                # A current meeting is ending
                used_rooms -= 1
                e += 1
            res = max(res, used_rooms)

        return res 

#HEAPQ SOLUTION
import heapq

class Solution:
    def min_meeting_rooms(self, intervals) -> int:
        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key= lambda x: x.start)

        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0].end)

        # For all the remaining meeting rooms
        for i in intervals[1:]:

            # If the latest (minHeap) room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i.start:
                heapq.heappop(free_rooms)

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i.end)

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)

'''
ex. [(0,30), (5,10), (15,20)]

heapq = [30] 
enters loop, doesn't fulfil if condition
heapq = [10,30]
next meeting, fulfills the condition 10 < 15
heapq = [20,30]
return length of heapq = 2
'''