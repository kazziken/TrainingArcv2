'''
Given a string 's' containing the characters '(' ,')', '{', '}', 
'[' , ']', determine if the input string is valid

Valid if open brackets must be closed by the same type of brackets
and closed in the correct order.

Ex.
s = '()'
output: true

s = "(){}[]"
output: true

'''

def valid_parenthesis(s):

    mapping = { '}' : '{', ')':'(', ']': '['}

    stack = []

    for c in s:
        #if its not a key, which means its an opening bracket,
        # add it to the stack
        if c not in mapping:
            stack.append(c)
            continue
        #if stack is still full or stacks value isn't == to the
        #opening bracket to match it return False
        if not stack or stack[-1] != mapping[c]:
            return False
        stack.pop()
    return stack == []
