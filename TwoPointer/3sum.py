'''

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k and nums[i] + nums[j] + nums[k] = 0

'''

def threeSum(nums):
    
    # nums = [2,5,8,-2,-5,-8,2,-2]
    
    nums.sort()
    
    res = []
    
    for i,v in enumerate(nums):
        # checks to see if v is the same as the previous element
        if i > 0 and v == nums[i-1]:
            continue
        
        #two pointer
        l, r = i + 1, len(nums) - 1
        
        while l < r:
            
            three_sum = v + nums[l] + nums[r]
            
            if three_sum < 0:
                l += 1
            elif three_sum > 0:
                r -= 1
            else:
                res.append([v, nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
    return res

'''

'''