#!/usr/bin/python
# https://practice.geeksforgeeks.org/problems/maximum-index/0

import sys

def sol(arr, n):
    ma = [None for i in range(n)]
    mi = [None for i in range(n)]
    
    mi[0] = arr[0]
    for i in range(1, n):
        mi[i] = min(arr[i], mi[i-1])
    
    ma[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        ma[i] = max(arr[i], ma[i+1])
    
    i=0; j=0
    md = -1*sys.maxsize

    #import pdb; pdb.set_trace()
    while i<n and j<n:
        if mi[i] <= ma[j]:
            # Careful about the equal to condition
            md = max(md, j-i)
            j+=1
        else:
            i+=1
    
    return md if md != -1*sys.maxsize else 0

arr = [5, 3, 19, 20, 2, 4]
print(sol(arr, len(arr)))