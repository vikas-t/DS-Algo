#!/usr/bin/python
#https://practice.geeksforgeeks.org/problems/convert-array-into-zig-zag-fashion/0

def sol(arr, n):
    """
    Keep swapping elements according to the order
    0/0 is not defined.
    """
    for i in range(n-1):
        if (i+1)%2 == 0:
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        else:
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    print(" ".join(str(x) for x in arr))