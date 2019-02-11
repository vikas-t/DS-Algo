#!/usr/bin/python
# https://practice.geeksforgeeks.org/problems/wave-array/0

def sol(arr, n):
    arr.sort()
    if n%2 != 0:
        r=n-1
    else:
        r = n
    for i in range(0, r, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    for x in arr:
        print(x, end=" ")
    print()