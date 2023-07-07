'''
You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

'''

from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        #creates a dictionary, key is the char and value is the frequency
        count1, count2 = Counter(s), Counter(t)

        #finding the difference in characters from each dict
        #first (count1 - count2) returns the difference in characters for count1
        #second(count2- count1) returns characters diff in count2
        #put them together in a new dict
        diff = (count1 - count2) + (count2 - count1)

        #take the total of all the values in that new dict and //2 to get the least amount of steps
        total_steps = sum(diff.values())//2
        return total_steps