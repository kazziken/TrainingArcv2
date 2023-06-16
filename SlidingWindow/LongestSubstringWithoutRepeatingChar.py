'''

Given a string s, find the length of the longest substring without repeating characters.

s= 'abcabcbb'
output : 3

s = 'bbbbb'
output : 1

'''

def no_repeating_char(self, s):

    l, r = 0
    res = 0
    visited = set()
    
    while r < len(s):
        if s[r] not in visited:
            visited.add(s[r])
            r += 1
            res = max(res , r - l)
        #s[r] is already in visited set
        else:
            #moves s[l] over to s[r] starting the new window and 
            while s[l] != s[r]:
                visited.remove(s[l])
                l += 1
            l += 1
            r += 1
    return res
