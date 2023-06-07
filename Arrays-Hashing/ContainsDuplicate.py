"""

Given an integer array [nums], return True if any value appears twice in the array, and return False
if every element is distinct

"""

"""

Explanation:
initialize a set - start adding each num in nums into set.
Will automatically run into dupe if the if statement runs:
returning True

"""

def contains_duplicate(self, nums):

    only_one_allowed = set()

    for num in nums:
        if num in only_one_allowed:
            return True
        only_one_allowed.add(num)
    return False