#!/usr/bin/python
# https://practice.geeksforgeeks.org/problems/find-equal-point-in-string-of-brackets/0

def sol(s):
    """
    Build an aux array from left that stores the no. 
    of opening brackets before that index
    Build an aux array from right that stores the no. of closing 
    brackets from that index
    Compare the two for a given index 
    """
    n = len(s)
    op_left = [0]*n
    cb_right = [0]*n
    
    for i in range(1, n):
        op_left[i] = op_left[i-1] + 1 if s[i-1] == "(" else op_left[i-1]
    # before that point so we check for s[i-1] instead of s[i]

    if s[n-1] == ")":
        cb_right[n-1] = 1
    for i in range(n-2, -1, -1):
        cb_right[i] = cb_right[i+1] + 1 if s[i] == ")" else cb_right[i+1]
    
    for i in range(n):
        if op_left[i] == cb_right[i]:
            return i
    
    return n