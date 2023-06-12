'''

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally indentical and the nodes have the same value

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def same_tree(self, p, q):

    if not p and q:
        return True

    if not p or not q or p.val != q.val:
        return False
    
    return (
        self.same_tree(p.left, q.left),
        self.same_tree(p.right, q.right)
    )