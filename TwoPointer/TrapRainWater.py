'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.

'''


def trap(height):

    l, r = 0, len(height) - 1
    l_max, r_max = height[l], height[r]
    total_water = 0 

    while l < r:
        if height[l] < height[r]:
            l += 1
            #update l_max while traversing
            l_max = max(l_max, height[l])
            total_water += (l_max - height[l])
        else:
            r -= 1
            r_max = max(r_max, height[r])
            total_water += (r_max - height[r])
    return total_water
            