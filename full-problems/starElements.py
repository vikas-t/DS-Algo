#!/usr/bin/python
# https://practice.geeksforgeeks.org/problems/start-elements/0

def sol(arr, n):
    """
    Beginning from the last keep a track of max till here, it the index is
    same as the max till here index include it in the result
    Do the same from left to right
    The common b/w the left and right are the 
    """
    se = []
    lse = []
    
    mai = n-1
    se.append(n-1)
    for i in range(n-2, -1,  -1):
        if arr[i] > arr[mai]:
            mai = i
        if mai == i:
            se.append(i)
    

    mii = 0
    lse.append(0)
    for i in range(1, n):
        if arr[i] > arr[mii]:
            mii = i
        if mii == i:
            lse.append(i)

    
    for i in range(len(se)-1, -1, -1):
        print(arr[se[i]], end=" ")
    print()
    
    r = False
    for x in se:
        if x in lse:
            print(arr[x], end=" ")
            r = True
    if  not r:
        print(-1)
    else: