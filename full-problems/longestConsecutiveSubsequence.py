#!/usr/bin/python3
#https://practice.geeksforgeeks.org/problems/longest-consecutive-subsequence/0

import sys
def sol(arr, n):
    """
    Sort the array and check for continuity
    """
    arr = sorted(arr)
    mc = 1
    i = 0
    c = 1
    while i <= n-2:
        if arr[i+1] == arr[i]+1:
            c+=1
        else:
            c=1
        mc = max(mc, c)
        i+=1
    return mc