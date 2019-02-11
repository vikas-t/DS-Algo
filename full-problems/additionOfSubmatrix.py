#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/addition-of-submatrix/0

for _ in range(int(input()))
    m, n = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    p, q, r, s = list(map(int, input().split()))
    k = 0
    res = 0
    for i in range(m):
        for j in range(n):
            if p <= i+1 <= r and q <= j+1 <= s:
                res+=arr[k]
            k+=1
    print(res)