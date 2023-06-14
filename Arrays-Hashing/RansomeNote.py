'''
Given two strings ransomNote and magazine, return true if ransomNote can 
be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Input: ransomNote = "a", magazine = "b"
Output: false

input: ransomNote = 'aa' magazine = 'ab'
output: false

input ransomNote = 'aa' magazine 'aab'
output: true

'''
from collections import Counter

def can_construct(ransom, magazine):

    d1, d2 = Counter(ransom), Counter(magazine)
    print(d1)
    print(d2)

    for key,val in d1.items():
        #if ransom key isn't found in magazine immediately return False
        if key not in d2:
            return False
        #else if d2 amount of tht specific key is less than the ransom value also return False
        else:
            if d2[key] < val:
                return False
    return True


print(can_construct('ab', 'ab'))

