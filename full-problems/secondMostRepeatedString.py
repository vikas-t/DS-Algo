#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/second-most-repeated-string-in-a-sequence/0
def sol(arr, n):
    h = {}
    for x in arr:
        h[x] = h[x] + 1 if x in h else 1
    t = sorted(h.items(), key=lambda x: x[1])
    return t[-2][0]
    