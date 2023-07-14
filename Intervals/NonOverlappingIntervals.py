'''
Given an array of intervals intervals where intervals[i] = [start[i], end[i]], 
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

'''
def not_overlapping(intervals):

    intervals.sort()
    res = 0
    prev_end = intervals[0][1]

    for start,end in intervals[1:]:
        # if no overlapping
        if start >= prev_end:
            prev_end = end
        else:
        # theres overlapping, so we'll increment res (to remove) and take the min end 
        # so we can keep the minimum amount of removal lower.
            res += 1
            prev_end = min(end, prev_end)
    return 
