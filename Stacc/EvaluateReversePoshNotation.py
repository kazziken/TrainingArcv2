'''

'''

def evaluateRPN(self, tokens):
    
    stack = []
    
    for c in tokens:
        if c == "+":
            stack.append(stack.pop() + stack.pop())
        elif c == "-":
            a, b = stack.pop(), stack.pop()
            #subtract the first token from the second (since b is the value that was already inside the stack)
            stack.append(b - a)
        elif c == "*":
            stack.append(stack.pop() * stack.pop())
        elif c == "/":
            a, b = stack.pop(), stack.pop()
            #wrapping it in int() rounds towrds zero instead of rounding down
            stack.append(int(b/a))
        else:
            stack.append(int(c))
    return stack[0]