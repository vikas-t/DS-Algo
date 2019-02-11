#!/usr/bin/python3
# https://www.geeksforgeeks.org/sort-a-stack-using-recursion/

# Sorted stack

def insert(stack, v):
    if not stack or v > stack[-1]:
        stack.append(v)
    else:
        t = stack.pop()
        insert(stack, v)
        stack.append(t)

def sort(stack):
    if stack:
        t = stack.pop()
        sort(stack)
        insert(stack, t)

# Driver code
x = [7,2,1,9,5]
sort(x)
print(x)