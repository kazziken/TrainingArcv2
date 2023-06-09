'''
Given an array of integers 'nums' which is sorted in ascending order,
and an integer 'target', write a function to search target in nums.
If target exists, then return its index. Otherwise return -1

'''

def binary_search(nums, target):
    l, r = 0, len(nums)-1

    while l <= r:
        mid = r + l // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1