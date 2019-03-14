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
        # At any time we are concerned about how many platforms are required
        # Careful when trains are arriving and departing at the same time !
            i+=1
            p += 1
            res = max(res, p)
        else:
        # If at any time the no, of platforms are not sufficient we need a 
        # new platform but if there are enough platforms the existing
        # requirement reduces by 1 at that moment
            p-=1
            j+=1
    return res