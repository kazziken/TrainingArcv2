'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

'''
'''
[3,9,20,null,null,15,7]

q = [3]
puts it in val [3]
now put it in res = [[3]]
has node.left and node.right[9,20] put that in q

q = [9,20] popleft [20] , val = [9], popleft again, val = [9,20] , 20 has node.left(15) and node.right(7) add to q
q = [15,7] 
now append val to res
res = [[3], [9,20]]

q = [15,7], popleft[15] , no n.left or n.right, popleft[7], no n.left,n.right,
val = [15,7]
res.append([15,7])
res = [[3],[9,20], [15,7]]
output res because q is empty
'''

# Definition for a binary tree node.
import collections

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def levelOrder(self, root):
        
        queue = collections.deque()
        
        if root:
            queue.append(root)
            
        res = []
        
        while queue:
            val = []
            
            for _ in range(len(queue)):
                node = queue.popleft()
                val.append(node.val)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            res.append(val)
        return res