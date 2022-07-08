#!/usr/bin/env python3
def balanced(expression):
    stack = []
    opening = set('(')
    closing = set(')')
    pair = {')' : '('}
    for i in expression:
        if i in opening:
            stack.append(i)
        if i in closing:
            if not stack:
                return False
            elif stack.pop() != pair[i]:
                return False
            else:
                continue
    if not stack:
        return True
    else:
        return False
    

print(balanced(input()))

