'''
Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1)..

Example:
input: nums = [3,4,5,2]
output: 12
Explanation: 4 and 5 are the two largest nums. return (4-1) * (5 - 1) = 3 *4 = 12

'''

def maxProduct(nums):

    first_max, second_max = 0

    for num in nums:
        if num > first_max:
            #set second_max to current first_max
            second_max = first_max
            first_max = num
        elif num > second_max:
            second_max = num
    
    return (first_max - 1) * (second_max - 1)

