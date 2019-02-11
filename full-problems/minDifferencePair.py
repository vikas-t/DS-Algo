#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/minimum-difference-pair/0

import sys

def sol(arr, n):
    """
    Sort the array and keep taking the diff. of current element with the next
    one, update the result
    """
    arr.sort()
    mn = sys.maxsize
    for i in range(n-1):
        mn = min(mn, arr[i+1]-arr[i])
    return mn