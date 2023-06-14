'''
Given two binary strings a and b, return their sum as a binary string.

Input: a = "11", b = "1"
Output: "100"

explanation: a = 3 b = 1 so 3 + 1 = 4
binary for 4 is 100

'''

def add_binary(self, a, b):

    carry = 0
    result = ''

    a = list(a)
    b = list(b)

    while a or b or carry:

        if a:
            carry += int(a.pop())
        if b:
            carry += int(b.pop())
        
        result += (str(carry % 2))
        carry //= 2
    return result[::-1]