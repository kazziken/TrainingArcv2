'''
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

'''

def longestCommonSequence(self, str1, str2):
    #2D array, need to do +1 on both strings to hit OOB and set them as 0
    dp = [[0 for j in range(len(str2 + 1))] for i in range(len(str1) + 1)]
    
    for i in range(len(str1) - 1, -1, -1):
        for j in range(len(str2) - 1, -1 , -1):
            #if its the same character go diagonal to continue else check to the right or below
            if str1[i] == str2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i][j + 1], dp[i + 1], dp[j])
    
    #since this is bottom-up the answer will be in the first index [0][0]
    return dp[0][0]

