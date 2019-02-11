#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/check-set-bits/0

def sol(n):
    while n:
        if n&1 == 0:
            print("NO")
            f = True
            break
        n=n>>1
    if not f:
        print("YES")

def sol(n):
    print("YES") if n&(n+1)==0 else print("NO")