#!/usr/bin/python
# https://practice.geeksforgeeks.org/problems/maximum-rectangular-area-in-a-histogram/0

import sys

def sol(arr, n):
    """
    For every bar, check the no. of bars greater or equal to its length
    on the left and the right side and multiply the count with the height
    of the bar to get the rectangle formed by that bar
    Complexity is n^2
    """
    area = -1*sys.maxsize
    for i in range(n):
        l = i-1
        r = i+1
        c = 1
        while l >= 0 and arr[l] >= arr[i]:
            c+=1
            l-=1
        
        while r < n and arr[r] >= arr[i]:
            c+=1
            r+=1
        area = max(area, arr[i]*c)
    
    return area