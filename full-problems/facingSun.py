#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/facing-the-sun/0

def sol(arr, n):
    """
    Create an auxiliary array that stores the index of the building which is 
    tallest till that index. For any building if the tallest bulding is at the
    same index(same building) it can recieve sunlight
    """
    res = 0
    lmax = [None for _ in range(n)]
    lmax[0] = 0
    # The first building receives the sunlight always
    for i in range(1, n):
        if arr[i] > arr[lmax[i-1]]:
            lmax[i] = i
        else:
            lmax[i] = lmax[i-1]
    # If the current building is taller than the previous lmax store the
    # current index otherwise store the previous lmax
    
    #print(lmax)
    for i in range(n):
        if i == lmax[i]:
            res+=1
    
    return res
    