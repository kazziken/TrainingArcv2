'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

'''

def sortColors(self, nums):

    lo = mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            #swap elements
            #example in this case nums[lo] == 1 and nums[mid] == 0 , [1,0], becomes [0,1]
            nums[lo], nums[mid] = nums[mid], nums[lo]
            lo += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1