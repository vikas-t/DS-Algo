#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/maximum-difference/0

def sol(arr, n):
    d = -1
    min_i = 0
    min_till_here = 0
    for i in range(1, n):
        if arr[i] < arr[min_till_here]:
            min_till_here = i
        if min_till_here != min_i and min_till_here < i:
            min_i = min_till_here
        d = max(d, arr[i]-arr[min_i])
    return d

arr = [5, 15, 3, 4, 5, 14]
print(sol(arr, len(arr)))