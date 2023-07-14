'''
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and 
intervals is sorted in ascending order by start[i]. 
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by start[i] and intervals still does not have any overlapping intervals 
(merge overlapping intervals if necessary).

Return intervals after the insertion.

Example:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

'''

def insertIntervals(intervals, newIntervals):

    res_array = []

    for i in range(len(intervals)):
        if intervals[i][0] > newIntervals[1]:
            # no overlapping 
            res_array.append(newIntervals)
            return res_array + intervals[i:]
        elif intervals[i][1] < newIntervals[0]:
            #newIntervals belongs on the right side, add intervals and continue
            res_array.append(intervals)
        else:
            #there is overlapping, make new newIntervals
            newIntervals = [
                min(newIntervals[0], intervals[i][0]),
                max(newIntervals[1], intervals[i][1])
            ]
    res_array.append(newIntervals)
    return res_array
