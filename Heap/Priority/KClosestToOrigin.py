'''

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,

return the k closest to the points to the origin (0,0)

The distance b/w two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).


'''

import heapq

def kClosest(self, points, k):

    minHeap = []

    for x, y in points:
        #don't need to od the whole √(x1 - x2)2 + (y1 - y2)2 since origin is (0, 0) its gonna return x**2, y**2
        dist = (x**2) + (y ** 2) 
        minHeap.append([dist, x, y])

    heapq.heapify(minHeap)
    res = []
    while k > 0:
        dist, x, y = heapq.heappop(minHeap)
        res.append([x,y])
        k -= 1
    
    return res 

'''
Explanation:

minHeap array to keep the smallest first index (smallest distance first index)

append it to the heap then pop them 

while K > 0
append [x,y] to the result to return the closest point to origin 
'''