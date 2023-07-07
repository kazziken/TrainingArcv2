'''
You are given a string s and an integer k. 
You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.


Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0
        char_count = {}

        most_freq_char = 0
        l = 0
        
        #when we're subtracting window length (r = the iteration not the index)
        for r in range(len(s)):
            
            char_count[s[r]] = char_count.get(s[r], 0) + 1
            most_freq_char = max(most_freq_char, char_count[s[r]])
            
            # r - l + 1 is the window length 
            if (r - l + 1) - most_freq_char > k:
                char_count[s[l]] -= 1
                l += 1
            res = max(res, (r - l + 1))
        return res
            
'''
Code Explanation:

variables:
res = to return answer
char_count = dict key:character value: frequency of the character
most_freq_char = to keep track of the highest freq 
if we subtract the length of the window from the substring, it should be == to k to return res

traverse the string while adding to char_count,
while keeping the most freq character count of the substring


if the window - most_freq_char ever <= k: we've gone over the limit and time to make the window smaller and take the char
out of the dictionary

res is only calculated when the window is smaller than/equal to k or we've reached the end of the string

'''