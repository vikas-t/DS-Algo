#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/type-of-array/0

def sol(arr, n):
    """
    Idea is to detect the first place where order has changed i.e increasing
    has become decreasing
    The tricky part is when the first 3 elements change order, in such cases
    check which side is bigger
    """
    ptype = None
    type = None
    
    for i in range(n-1):
        if arr[i+1] == arr[i]:
            continue
        
        type = 1 if arr[i+1] > arr[i] else 2
        
        if ptype and type != ptype:
            # If the last type is not same as current type array has rotated
            if ptype == 1:
                mx = arr[i]
                if arr[i+1] > arr[i-1]:
                    type = 3
                else:
                    type = 4
            # The first three elements are 10, 20, 5
            # A bigger element sanwiched b/w two smaller elements
            else:
                if arr[i+1] > arr[i-1]:
                    mx = arr[i+1]
                    type = 3
                else:
                    mx = arr[i-1]
                    type = 4
            # The first three elements 70, 4, 34
            # A smaller element sandwiched b/w two bigger elements
            break
        ptype = type
    
    if type == 1:
        mx = arr[-1]
    elif type == 2:
        mx = arr[0]
    
    return mx, type