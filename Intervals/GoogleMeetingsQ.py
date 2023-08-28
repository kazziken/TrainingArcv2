"""
You are given an array of time slot requests for meetings.

Return a map of meeting room to time slots which uses the least amount of rooms.

Example:
Input : [ (r1, 8am, 9am), (r2, 9am, 12pm), (r3, 8:30am, 10am) ]
Output: { room1: [r1, r2], room2: [r3] }

"""
import heapq
from collections import defaultdict

def Solution(meetings):
    
    meetings.sort(key=lambda x:x[1])

    res = defaultdict(list)

    rooms = []
    room_id = 0
    for i, start, end in meetings:
        if rooms and rooms[0][0] <= start:
            room_end, existing_room_id = heapq.heappop(rooms)
            res[existing_room_id].append(i)
            heapq.heappush(rooms, (end, existing_room_id))
        else:
            room_id += 1
            res[room_id].append(i)
            heapq.heappush(rooms, (end, room_id))

    return res
