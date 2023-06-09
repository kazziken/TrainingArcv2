'''

A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric chars,
it reads the same forward and backwrd.

Given a string 's', return if its a palindrome, or false otherwise.
'''

'''
Explanation:
2 pointer beginner question:
l always starts at the beginning of s
r starts at the end
since there is a possiblity of non-alphanumerical chars in s,
in our while loop we first make sure if l or r is not .isalnum()
move pointer:

finally, make sure to match while .lower().
else:
    move the pointers and return True as a default
'''

def valid_palindrome(s):

    l, r = 0, len(s) -1

    while l <= r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        else:
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
    return True