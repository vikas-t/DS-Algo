#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/extract-maximum/0

def sol(s, n):
    """
    If the character is a number and l is not set set it to that index, if it
    is set the r.
    If character is not a number set both l and r as None
    """
    l = None
    r = None
    mx = 0
    for i in range(n):
        if 48 <= ord(s[i]) <= 57:
            if l == None: 
            # Be careful when saying "not X" keeping in mind 0 is False
                l = i
            r = i
            mx = max(mx, int(s[l:r+1]))
        else:
            l = None
    return mx