'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time smallest_elementults in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.



'''

def minimum_rotated_search_array(nums):
    
    l, r = 0, len(nums) - 1
    #varible to hold smallest element 
    smallest_element = nums[0]
    
    
    # example: [3,4,5,1,2]
    while l <= r:
        if nums[l] < nums[r]: #we only need to consider left side, else we need to consider right side
            smallest_element = min(smallest_element, nums[l])
            # we already found the smallest element b/c it is ascending. If the num on the left is ever lower, thats the smallest
            break

        mid = (l + r) // 2
        smallest_element = min(smallest_element, nums[mid])
        
        #its on the right side, mid is closest to the largest element
        if nums[mid] >= nums[l]:
            l = mid + 1
        else:
            r = mid - 1
    return smallest_element
    
        
            
            