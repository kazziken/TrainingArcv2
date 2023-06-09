'''
Given the root of a binary tree, invert the tree, and return its roots

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_binary_tree(self, root):

    if not root:
        return None

    temp = root.right
    root.right = root.left
    root.left = temp

    #run it for child nodes
    self.invert_binary_tree(root.left)
    self.invert_binary_tree(root.right)

    return root