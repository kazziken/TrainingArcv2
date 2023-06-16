'''
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.


'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
def max_path_level(self, root):
    dic = collections.defaultdict(int)
    
    def dfs(root,level):
        
        if root is None:
            return 

        dic[level] += root.val # add to the total of that level
        dfs(root.left, level+1)
        dfs(root.right, level + 1)
    
    #call the function
    dfs(root, 1)
    #create a max counter
    maximum = float('-inf')
    #start at level 1
    level = 1
    
    for i in dic:
        if dic[i] > maximum:
            #update the max
            maximum = dic[i]
            level = i
    return level
    
    