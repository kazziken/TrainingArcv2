'''
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

Example:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
'''


#BRUTE FORCE IS THE SOLUTION (RECURSION/Backtracking) Decision Tree, Height of the decision tree is K
#time complexity is worst O(n) best case is O(K* n^k)
def combine(self, n, k):

    res = []

    def helper(start, combination):
        if len(combination) == k:
            res.append(combination.copy())
            return
        #our decision tree
        for i in range(start, n + 1):
            combination.append(i)
            helper(i + 1, combination)
            #pop to create more combinations
            combination.pop()
    helper(1, [])
    return res


        
'''Explanation:
the helper function is the dfs function that helps backtrack all of the possible combinations

'''