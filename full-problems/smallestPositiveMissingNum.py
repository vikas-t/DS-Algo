#!/usr/bin/python
# https://practice.geeksforgeeks.org/problems/smallest-positive-missing-number/0


def sol(arr, n):
    m = max(arr)
    h = [0]*(m+1)
    for x in arr:
        if x < 0:
            continue
        h[x] = h[x]+1
    
    found = False
    for i in range(1, m+1):
        if h[i] == 0:
            found = True
            r = i
            break
    
    if not found:
        return m+1
    else:
        return r