#!/usr/bin/python

#https://practice.geeksforgeeks.org/problems/overlapping-rectangles/0

def sol(f, s):
    fx1, fy1, fx2, fy2 = f
    sx1, sy1, sx2, sy2 = s
    
    if fx1 > sx2 or sx1 > fx2:
        return 0
    
    if fy2 > sy1 or sy2 > fy1:
        return 0
    return 1