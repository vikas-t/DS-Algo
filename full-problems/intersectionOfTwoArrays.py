#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/intersection-of-two-arrays/0

def sol(a, b, m, n):
    ah = {}
    bh = {}
    res = []
    for x in a:
        ah[x] = True
    
    for x in b:
        bh[x] = True
    
    for x in ah:
        if x in bh:
            res.append(x)
    
    for x in sorted(res):
        print(x, end=" ")
    
    if res:
        print()
    else:
        print("Zero")