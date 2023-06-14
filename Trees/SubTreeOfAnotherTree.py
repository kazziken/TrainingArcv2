'''
Given the roots of two binary tree root and subRoot, return true if there is
a subtree of root with the same structure and node values of subRoot and false
otherwise.

A subtree of binary tree 'tree' is a tree that consists of a node in tree and
all of these node's descendants. The tree could also be considered a subtree of itself

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def subtree_of_another_tree(self, root, subRoot):

    if not root:
        return False
    
    if not subRoot:
        return True
    
    if self.same_tree(root, subRoot):
        return True
    
    return (self.subtree_of_another_tree(root.left, subRoot) or
            self.subtree_of_another_tree(root.right, subRoot)
            )
    
def same_tree(self, root, subRoot):

    if not root and not subRoot:
        return True
    
    if not root or not subRoot:
        return False
    
    if root and subRoot and root.val == subRoot.val:
        return (self.same_tree(root.left, subRoot.left),
                self.same_tree(root.right, subRoot.right)
                )
    else:
        return False