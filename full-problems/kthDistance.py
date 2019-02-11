#!/usr/bin/python3
#https://practice.geeksforgeeks.org/problems/kth-distance/0

def sol(arr, n, k):
    """
    Store the position of the element in a hash and keep updating it 
    as we go forward. If the element already exists in the hash check 
    the distance between them and return True if it is <= k
    """
    h = {}
    for i in range(n):
        if arr[i] in h:
            pos = h[arr[i]]
            if pos+k >= i:
                return True
        h[arr[i]] = i
    
    return False