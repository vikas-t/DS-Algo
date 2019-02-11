#!/usr/bin/ptyhon3
# https://practice.geeksforgeeks.org/problems/palindromic-array/0

def sol(arr, n):
    """
    We try and go close to the number on the ends by adding the element
    with its adjacents
    """
    l = 0
    r = n-1
    res = 0
    
    while  l < r:
        if arr[l] == arr[r]:
            l+=1
            r-=1
        elif arr[l] > arr[r]:
            r-=1
            arr[r] += arr[r+1]
            res+=1
        else:
            l+=1
            arr[l] += arr[l-1]
            res+=1
    return res