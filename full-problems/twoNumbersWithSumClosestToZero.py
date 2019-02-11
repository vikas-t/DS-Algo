#!/usr/bin/python

# https://practice.geeksforgeeks.org/problems/two-numbers-with-sum-closest-to-zero/0

import sys

def sol(arr, n):
    """
    Comlexity is n^2
    """
    res = []
    dMin = sys.maxsize
    
    for i in range(n-1):
        for j in range(i+1, n):
            s = arr[i] + arr[j]
            if abs(s) < dMin:
                dMin = abs(s)
                res = [sorted((arr[i], arr[j]))]
            elif abs(s) == dMin:
                res.append(sorted((arr[i], arr[j])))

    res = sorted(res, key=lambda k: k[1], reverse=True)
    return res[0]

def sol2(arr, n):
    """
    Algorithm 
    1) Sort all the elements of the input array.
    2) Use two index variables l and r to traverse from left and right ends respectively. Initialize l as 0 and r as n-1.
    3) sum = a[l] + a[r]
    4) If sum is -ve, then l++
    5) If sum is +ve, then r–
    6) Keep track of abs min sum.
    7) Repeat steps 3, 4, 5 and 6 while l < r
    """
    pass