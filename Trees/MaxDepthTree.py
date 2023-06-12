'''
Given the root of a binary tree, return its maximum depth.

Max depth is the num of nodes along the longest path from the root node down to the farthest leaf node.

root = [3,9, 20, null,null,15,7]
output: 3

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def max_depth_tree(self, root):
    if not root:
        return None
    
    return 1 + max(
        self.max_depth_tree(root.left),
        self.max_depth_tree(root.right)
        )