#!/usr/bin/python3
#https://practice.geeksforgeeks.org/problems/index-of-first-1-in-a-sorted-array-of-0s-and-1s/0

for _ in range(int(input())):
    n = int(input())
    f = False
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        if arr[i] == 1:
            f = True
            print(i)
            break
    if not f:
        print(-1)