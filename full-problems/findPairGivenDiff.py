#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/find-pair-given-difference/0

def sol(arr, n, t):
    """
    Create a hash of the elements check if the diff+element exists in the
    hash
    """
    h = {}
    for x in arr:
        h[x] = True
    
    for x in arr:
        if t+x in h:
            return 1
    return -1