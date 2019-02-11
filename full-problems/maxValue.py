#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/max-value/0
import sys

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    d = []
    for i in range(n):
        d.append(arr[i]-i)
    d.sort()
    print(d[-1]-d[0])