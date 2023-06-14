'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.


Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.


'''

def longest_palindrome(s):

    hash_set = set()

    for c in s:
        if c not in hash_set:
            hash_set.add(c)
        else:
            hash_set.remove(c)

    if len(hash_set) != 0:
        return len(s) - len(hash_set) + 1
    else:
        return len(s)

