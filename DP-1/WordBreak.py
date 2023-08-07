'''
Given a string 's' and a dictionary 'wordDict', return True if s can be segmented into a space-separated
sequence of one or more dictionary words.

note that the same word in the dict can be reused multiple times in the segmentation

Ex 1:
s = 'leetcode' wordDict = ['leet', 'code']
output: True

'''

def wordBreak (s, wordDict):

    dp = [False] * (len(s) + 1) # +1 because the dp[len(s)] will be set to True
    dp[len(s)] = True

    for i in range(len(s) - 1, -1, -1):
        for w in wordDict:
            if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                dp[i] = dp[i + len(w)]
            if dp[i]:
                break
            
    return dp[0]