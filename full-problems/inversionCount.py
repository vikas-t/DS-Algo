#!/usr/bin/python

# https://practice.geeksforgeeks.org/problems/inversion-of-array/0

def sol(arr, n):
    c = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                c+=1
    return c