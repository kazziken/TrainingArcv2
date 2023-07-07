'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    def isValidBST(root):
        
        def helper(node, left, right):
            if not node:
                return True

            if not (node.val < right and node.val > left):
                return False
            
            
            # node.left is the children, left of left side, and node.val is the right of that
            return helper(node.left, left, node.val) and helper(
                #node.right is the children, node.val is the left side of that child, and right of right side)
                node.right, node.val, right
            )
            
        return helper(root, float('-inf'), float('inf'))

