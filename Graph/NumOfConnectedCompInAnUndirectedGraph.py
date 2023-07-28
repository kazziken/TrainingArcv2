'''
You have a grph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi]
indicates that there is an edge b/w ai and bi in the graph.
Return the number of connected components in the graph.

Example:
Input: n = 5, edges [[0,1], [1,2], [3,4]]
Output: 2

Explanation: 0,1,2 are connected to each other so thats one. 3,4 are connected.
 Output is 2 because there is 2 number of contiguous components.

UnionFind algorithm is designed for a O(e + v) time complexity

'''

def num_of_connected(n, edges):
    parent = [i for i in range(n)]
    rank = [1] * n

    def find(n1):
        res = n1
        
        while res != parent[res]:
            #this line will not execute if there is no grandparent
            parent[res] = parent[parent[res]]

            res = parent[res]
        return res

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)

        #if they have the same parent (no union)
        if p1 == p2:
            return 0
        
        if rank[p2] > rank[p1]:
            parent[p1] = p2
            rank[p2] += rank[p1]
        else:
            parent[p2] = p1
            rank[p1] += rank[p2]
        return 1
    
    res = n
    for n1, n2 in edges:
        res -= union(n1, n2) #if union is > 0 it will decrement from n
    return res


    


