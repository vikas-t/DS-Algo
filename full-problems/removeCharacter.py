#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/remove-character/0

def sol(a, b):
    """
    Maintain a hash of characters for both string and print the ones that 
    are there in first one and not second one
    """
    ha = {}
    hb = {}
    for x in a:
        ha[x] = True
    
    for x in b:
        hb[x] = True
    
    for x in a:
        if x not in hb:
            print(x, end="")
    print()