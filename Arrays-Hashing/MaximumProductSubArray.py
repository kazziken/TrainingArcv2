'''
Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.


example:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

'''

'''
Explanation: 
Brute force is to find every subarray and calculate the product

How can we do this efficiently?
Calculate the maximum and minimum.
Maximum keeps the largest value and minimum keeps the smallest value.
Maximum will factor iterating through the array with (n * min value) in case of double negative numbers.


'''


def maximum_product_subarray(nums):
    
    res = nums[0]
    curr_min, curr_max = 1, 1
    
    for n in nums:
        #so we can use the previous curr_max value when we calculate the curr_min
        temp = n * curr_max
        #(n * cur_max or n * min (if n and cur_max are both negative) or just n itself)
        curr_max = max(n * curr_min, n * curr_max, n)
        curr_min = min(temp, n * curr_min, n)
        res = max(res, curr_max)
    return res