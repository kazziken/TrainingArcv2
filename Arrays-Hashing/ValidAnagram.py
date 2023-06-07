"""

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

"""

"""
Explanation - map each word into its own hashmap
key: character, value: freq

return hash_s == hash_t will return True or False depending on if both hashmaps are the same
"""

def valid_anagram(self, s, t):

    hash_s = {}
    hash_t = {}

    for c in s:
        hash_s[c] = hash_s.get(c, 0) + 1
    
    for c in t:
        hash_t[c] = hash_t.get(c, 0) + 1

    return hash_s == hash_t