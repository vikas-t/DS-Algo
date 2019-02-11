#!/usr/bin/python3
#https://practice.geeksforgeeks.org/problems/amount-of-water/0

def sol(arr, n):
    """
    Water on any building will be stored if its left and right building 
    are taller than its height
    We use two aux arrays to find out the height of the tallest buildings 
    from both the sides
    """
    lmax = [0]*(n)
    rmax = [0]*(n)
    
    lmax[0] = arr[0]
    for i in range(1, n):
        lmax[i] = arr[i] if arr[i] > lmax[i-1] else lmax[i-1]
    # Create an auxiliary array that store the height of the tallest building
    # moving from left of the the array

    rmax[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        rmax[i] = arr[i] if arr[i] > rmax[i+1] else rmax[i+1]
    # Create an auxiliary array that store the height of the tallest building
    # moving from right to left

    res = 0
    for i in range(n):
        if lmax[i] > arr[i] and rmax[i] > arr[i]:
            res += (min(lmax[i], rmax[i])-arr[i])
    
    return res