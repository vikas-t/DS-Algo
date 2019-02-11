#!/usr/bin/python
# https://practice.geeksforgeeks.org/problems/find-first-set-bit/0

def sol(n):
    c = 1
    while n:
        if n&1:
            return c
        n=n>>1
        c+=1
    return 0