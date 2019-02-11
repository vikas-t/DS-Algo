#!/usr/bin/python3
#https://practice.geeksforgeeks.org/problems/binary-string/0

def sol(s):
    """
    Iterate over all the subtrings and count
    """
    n = len(s)
    c = 0
    for start in range(n-1):
        for end in range(start+1, n):
            if s[start] == '1' and s[end] == '1':
                c+=1
    return c