'''

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally indentical and the nodes have the same value

'''

'''
Explanation: 
How do we check if they're the same tree?
Base cases: if p and q don't exist - true
if only one of p or q exist - false

if both exist and values are the same, check both left and right of the nodes by recursively calling
if both the left and right subtrees are identical.

If any of the conditions are not satisfied, it means either p and q are not equal or one of them ins None
Returning False

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def same_tree(self, p, q):

    if not p and not q:
        return True

    if not p or not q:
        return False
    
    if p and q and p.val == q.val:
        return self.same_tree(p.left, q.left) and self.same_tree(p.right, q.right)
    else:
        return False