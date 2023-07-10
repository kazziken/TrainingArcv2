'''
Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.


Example:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

'''


def mergeIntervals(self,intervals):

    #we're assuming the first indices of each aren't sorted so lets do that
    intervals.sort(key = lambda i : i[0])

    #since we're always going to need the first index to continue
    output = [intervals[0]]

    for start,end in intervals[1:]:
        last_end = output[-1][1]
        
        '''
        checking next iteration if their start is less than the last_end of the previous iteration
        if it is , its overlapping, so we're going to replace the last_end value as the max of both ends
        '''
        if start <= last_end:
            output[-1][1] = max(last_end, end)
        else:
            output.append([start,end])
    
    return output



