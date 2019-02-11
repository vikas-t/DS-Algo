#!/usr/bin/python
#https://practice.geeksforgeeks.org/problems/floor-in-a-sorted-array/0
def sol(arr, n, k):
    f = None
    for i in range(n):
        if arr[i] <= k:
            f = i
    if not f:
        return -1
    return f