#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/uncommon-characters/0


def sol(s1, s2):
    """
    Straight forward hashin approach, Sets can also be used
    """
    h1 = {}
    h2 = {}
    
    for x in s1:
        h1[x] = True
    
    for x in s2:
        h2[x] = True
    
    res = []
    for x in h1:
        if x not in h2:
            res.append(x)
    
    for x in h2:
        if x not in h1:
            res.append(x)
    
    for x in sorted(res):
        print(x, end="")
    print()