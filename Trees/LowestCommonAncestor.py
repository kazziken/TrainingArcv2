'''
'Given a BST and find the LCA of two given nodes in the BST

LCA is defined between two nodes 'p' and 'q' as the lowest nodes in T that has both p and q as descendants


'''

'''
Explanation

p,q are just random nodes. think in terms of a BST. 

If both p and q are < current node. then the smallest node is currently on the left subtree to find the lowest common ancestor
If both p and q are > current node, then we go down the right subtree to find the lowest common ancestor

else:
    p is > and q is < than current_node (finding p or q or the split)
    which is the lowest common ancestor so return current
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowest_common_ancestor(self, root, p, q):

    # current_node = root

    # while current_node is not None:
    #     if p.val > current_node.val and q.val > current_node.val:
    #         current_node = current_node.right
    #     elif p.val < current_node.val and q.val < current_node.val:
    #         current_node = current_node.left
    #     else:
    #         return current_node


    if root == None or root == p or root == q:
            return root
        
    l = self.lowestCommonAncestor(root.left, p, q)
    r = self.lowestCommonAncestor(root.right, p, q)

    #if nothing was found on left side, check right
    if not l:
        return r
    
    #vise versa
    if not r:
        return l
    
    else:
        return root
