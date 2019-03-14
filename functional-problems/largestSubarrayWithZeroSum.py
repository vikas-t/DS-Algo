#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1

def maxLen(n, arr):
    """
    The idea is to iterate through the array and for every element arr[i], 
    calculate sum of elements form 0 to i (this can simply be done as sum += arr[i]). 
    If the current sum has been seen before, then there is a zero sum array. 
    Hashing is used to store the sum values, so that we can quickly store sum 
    and find out whether the current sum is seen before or not.
    """
   
    maxLn = 0
    h = {}
    
    sth = 0
    for i in range(n):
        sth += arr[i]
        
        if arr[i] == 0:
            maxLn = max(1, maxLn)
        # If the element itself is 0, length is 1
        
        if sth == 0:
            maxLn = i+1
        # If the sum till current index is 0, then the entire length becomes
        # the max length
        
        if sth not in h:
            h[sth] = i
        else:
            ln = i - h[sth]
            maxLn = max(maxLn, ln)
    return maxLn