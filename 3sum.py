'''

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k and nums[i] + nums[j] + nums[k] = 0

'''

def threeSum(nums):
    
    nums.sort()
    
    #O(n log n time)
    res = []
    
    for i, v in enumerate(nums):
        
        if i > 0 and v == nums[i - 1]:
            continue
            
        #use two pointer
        l, r = 0, len(nums) - 1
        while l < r:
            three_sum = v + nums[l] + nums[r]
            
            if three_sum < 0:
                l += 1
            elif three_sum > 0:
                r -= 1
            else:
                res.append([v, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
    return res

'''


'''