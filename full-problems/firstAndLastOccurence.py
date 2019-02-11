#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/first-and-last-occurrences-of-x/0

for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    res = []
    i = 0
    while i < n and arr[i] <= k:
        if arr[i] == k:
            res.append(i)
        i+=1
    if res:
        print(res[0], res[-1])
    else:
        print(-1)