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
        
        if not intervals:
            return 0
        
        used_rooms = 0

        #Seprate the time and end timings, sorting them individually
        start_times = sorted([i.start for i in intervals])
        end_times = sorted(i.end for i in intervals)

        #2pointers
        start_p, end_p = 0, 0

        #until all the meetings have been iterated
        while start_p < len(intervals):
            # if there is a meeting that as ended by the time the meeting at 'start_p' starts
            if start_times[start_p] >= end_times[end_p]:
                # then free up a room and increment end pointer
                used_rooms -= 1
                end_p += 1
            used_rooms += 1
            start_p += 1
        return used_rooms

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