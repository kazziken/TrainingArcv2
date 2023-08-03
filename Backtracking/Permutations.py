'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
'''

'''
Example:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''

def permute(self, nums):

    res = []
    
    #base case
    if len(nums) == 1:
        # nums[:] is a deep copy
        return [nums[:]]
    
    for _ in range(len(nums)):
        #pop the first element out of the arr
        n = nums.pop(0)
        perms = self.permute(nums)

        #The permutations obtained from the recursive call are stored in the perms list.
        #append the popped element to the permutations of the recursive call of perms
        #example perms = [2,3] and [3,2]
        for perm in perms:
            perm.append(n)
        res.extend(perms)
        #re-add n back to the original arr and run that perms again until its done iterating
        #The loop continues until all elements in nums have been considered as the first element in the permutations.
        nums.append(n)
    return res


    #dfs way
def permutation(nums):
    res = []
    
    def dfs(nums, path, res):
        #if we're at a leaf node, add to res
        if not nums:
            res.append(path)
            # return # backtracking
        for i in range(len(nums)):
            #nums[:i]
            dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
    
    dfs(nums, [], res)
    return res