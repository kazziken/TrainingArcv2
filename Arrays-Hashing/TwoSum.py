"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

"""
explanation: You should just know this
"""

def two_sum(self, nums, target):

    hash_sum = {}

    for i,num in enumerate(nums):
        difference = target - num
        if difference in hash_sum:
            return [i, hash_sum[difference]]
        hash_sum[num] = i
    return []