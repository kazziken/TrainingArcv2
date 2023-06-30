'''

Given an integer array nums, find the 
subarray
with the largest sum, and return its sum.
 
'''

'''
Example:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

'''

def maximumSubarray(nums):
    
    if not nums:
        return 0
    
    #start with first index
    cur_sum = max_sum = nums[0] 

    for num in nums[1:]:
        
        cur_sum = max(num, num + cur_sum)
        max_sum = max(max_sum, cur_sum)
    return max_sum

'''
Explanation:

We'll use above nums array [-2,1,-3,4,-1,2,1,-5,4]
cur_sum = -2, max_sum = -2
num = 1, cur_sum = max(-2, -2 + 1)
update cur_sum = -1.
cur_sum = -1, max_sum = -1

using one variable to calculate sum of subarrays and one var to keep track of max sub seen so far.
can return max_sum when finish traversing through the array.
time complexity o(n) we're traversing the array
space o(1) we're using variables
'''