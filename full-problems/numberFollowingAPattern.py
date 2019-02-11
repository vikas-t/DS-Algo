#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/number-following-a-pattern/0

def sol(s):
    """
    Keep pushing the numbers on the stack and print till the stack is empty
    when an 'I' or end is found
    """
    n = len(s)
    stack = []
    
    for i in range(n+1):
        stack.append(i+1)
        if i == n or s[i] == 'I':
            while stack:
                x = stack.pop()
                print(x, end="")
    print()