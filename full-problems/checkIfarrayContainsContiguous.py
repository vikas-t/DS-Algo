#!/usr/bin/python
# https://practice.geeksforgeeks.org/problems/check-if-array-contains-contiguous-integers-with-duplicates-allowed/0

def sol(arr, n):
    """
    Let the count start from minimum instead if zero to save space
    """
    mn = min(arr)
    mx = max(arr)
    c = [0]*(mx-mn+1)
    
    for x in arr:
        c[x-mn] += 1
    
    for x in c:
        if not x:
            return False
    
    return True