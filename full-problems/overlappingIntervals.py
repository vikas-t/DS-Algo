#!/usr/bin/python3
#https://practice.geeksforgeeks.org/problems/overlapping-intervals/0
from functools import cmp_to_key

def comp(a, b):
    if a[0] > b[0]:
        return 1
    return -1

def sol(arr):
    n = len(arr)
    arr = sorted(arr, key=cmp_to_key(comp))
    # Sort the initial array so that we know that the next interval is equal
    # to or greater than the current one
    res = [] 
    # Lets maintain an array which we treat as a stack while pushing results
    res.append((arr[0][0], arr[0][1]))
    
    for i in range(1, n):
        l, r = arr[i][0], arr[i][1]
        ml, mr = res[-1]
    
        if l < ml and r < ml:
            # If the interval is smaller than the left limit then it canot
            # be merged and we push it beneath the top
            tmp = res.pop()
            res.append((l, r))
            res.append(tmp)
        elif l > mr and r > mr:
            # If the interval is greater than the right limit it cannot be
            # merged and we push it on top of the stack
            res.append((l, r))
        else:
            # Now, if the interval is not out of the limits, it needs to be
            # merged. So we take the farther end from both intervals and now
            # the new interval is going to replace the last one as the new top
            ml, mr = min(l, ml), max(r, mr)
            res.pop()
            res.append((ml, mr))
                
    for x in res:
        print(x[0], x[1], end=" ")
    print()