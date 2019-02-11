#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/largest-number-in-k-swaps/0

def maxOf(a, b):
    for i in range(len(a)):
        if a[i] > b[i]:
            return a
        elif a[i] < b[i]:
            return b
    return a

def bt(arr, k):
    """
    The backtrack solution where we try all cases and return the max.
    A greedy approach will not work here
    """
    global m
    #print(k, m, arr)
    if k == 0:
        return
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[j] > arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
                m = maxOf(m, arr)[:]
                bt(arr, k-1)
                arr[j], arr[i] = arr[i], arr[j]

m=[]
print("".join(str(x) for x in m))
# The global result list, notice we are not passing any variable 
# to store the result 

#**********************************************************************

def greedy(arr, n):
    """
    This is not going to work consider the two test cases that failed
    1)
    k=3
    n=4551711527

    Its Correct output is:
    7755511124

    And Your Code's output is:
    7755411125

    2)
    Input : 
    n = 61892795431
    k = 4
    Its Correct output is:
    99876215431

    And Your Output is:
    99876125431
    """
    n = len(arr)
    i = 0
    kc = 0
    while i < n and kc < k:
        mx = arr[i]
        mxi = None
        for j in range(i+1, n):
            if arr[j] >= mx:
                mx = arr[j]
                mxi = j
        if mxi:
            arr[i], arr[mxi] = arr[mxi], arr[i]
            kc+=1
        i+=1
    
    return "".join(str(x) for x in arr) 