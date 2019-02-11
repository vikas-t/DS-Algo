#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/positive-and-negative-elements/0

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    p = []
    n = []
    for x in arr:
        if x < 0:
            n.append(x)
        else:
            p.append(x)
    for i in range(len(p)):
        print(p[i], n[i], end=" ")
    print()