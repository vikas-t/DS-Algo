#!/usr/bin/python

#https://practice.geeksforgeeks.org/problems/unsorted-array/0

def sol(arr, n):
    """
    Idea is simple, while going from left to right keep a track of max 
    till i, thus all elements to the left of i are smaller.
    While going from right to left keep a track if min till i thus all 
    elements to the right are greater
    """
    ltr = [0]*n
    rtl = [0]*n
    
    ma = arr[0]
    for i in range(n):
        ma = max(arr[i], ma)
        ltr[i] = ma
    
    mi = arr[n-1]
    for i in range(n-1, -1, -1):
        mi = min(arr[i], mi)
        rtl[i] = mi
    
    for i in range(n):
        if ltr[i] == rtl[i] and i and i!=n-1:
            # Boundaries of 'i' are checked as we want atleast one element
            # on either side of the result
            return arr[i]
    
    return -1