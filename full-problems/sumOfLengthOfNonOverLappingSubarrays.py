#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/sum-of-lengths-of-non-overlapping-subarrays/0

def sol(arr, n, k):
    """
    Keep traversing right and updating start and end if the arr[i] <= k, 
    Set the flag if k is included in between the start and the end.
    Finally count the length if the flag is set
    """
    start = None
    end = None
    l = 0
    t = 0
    maxK = False
    
    for i in range(n):
        if arr[i] > k:
            t += l
            start = None
            maxK = False
            l = 0
        else:
            if start == None:
                start = i
            end = i
            if arr[i] == k:
                maxK = True
            
            if maxK:
                l = end-start+1
    t+=l
    # The last subarray needs to be counted as well
    return t