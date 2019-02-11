#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/minimum-platforms/0

def sol(a, d, n):
    p = 1
    res = 1
    a.sort()
    d.sort()
    
    
    i = 1
    j = 0
    while i < n and j < n:
        if a[i]  < d[j]:
        # Careful when trains are arriving and departing at the same time !
            i+=1
            p += 1
            res = max(res, p)
        else:
            p-=1
            j+=1
    return res