#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/unique-numbers/0

def isRepeat(s):
    h = {}
    for x in s:
        if x in h:
            return True
        else:
            h[x] = True
    return False
    
def sol(l,r):
    for x in range(l, r+1):
        s = str(x)
        if not isRepeat(s):
            print(s, end=" ")
    print()