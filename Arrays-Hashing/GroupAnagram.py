'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 

typically using all the original letters exactly once.
'''

'''

First initalize hashmap
we're going to sort each str
if key isn't already in dic, create an empty arr
append the unsorted str to that key

return values of each key which are the grouped anagrams

'''

def group_anagram(strs):

    dic = {}

    for str in strs:
        key = "".join(sorted(str))
        print(key)

        if key not in dic:
            dic[key] = []
        
        dic[key].append(str)
    return dic.values()


strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagram(strs))