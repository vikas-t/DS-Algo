#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/maximum-value-in-a-bitonic-array/0
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    found = False
    for i in range(n-1):
        if arr[i+1] < arr[i]:
            found = True
            print(arr[i])
            break
    if not found:
        print(arr[n-1])