#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/maximize-number-of-1s/0

def sol(arr, m, n):
    """
    The sliding approach
    """
    l = 0
    r = 0
    c = 0
    res = 0
    # Intialize left right and zero count to 0
    while r < n:
        if c <= m:
            if arr[r] == 0:
                c+=1
            r+=1
    # Keep moving right and if zero count is less than or equal to m increment
    # the zero count. This way we can exceed the zero count by 1
        
        if c > m:
            if arr[l] == 0:
                c-=1
            l+=1
    # If the zero count > m, and we have found a zero again we decrease the
    # count by one, basically saying drop the left zero and pick the right
    # one
            
        res = max(res, r-l)
    # Update the maximum window while sliding
    return res