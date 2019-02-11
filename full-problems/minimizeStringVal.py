#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/minimize-string-value/0

import sys

def findMax(sc, n):
    mx = -1*sys.maxsize
    mxi = None
    for i in range(n):
        if sc[i] > mx:
            mx = sc[i]
            mxi = i
    return mxi
        
def sol(s, k):
    """
    Keep finding the number with max frequency and decrease the frequency by 1
    Check the max heap solution as solved in gameWithStrings.py
    """
    c = {}
    
    for char in s:
        c[char] = c[char] + 1 if char in c else 1
    
    sc = sorted(list(c.values()))
    x = -1
    while k > 0 and sc[x] > 0:
        k -= 1
        sc[x] -= 1
        x = findMax(sc, len(sc))
    
    res = 0
    for x in sc:
        res = res + x**2
    return res

print(sol("sjybldbefsarcbynecdyggxxpklorellnmpapqfwkhop", 13))