#!/usr/bin/python3
#https://practice.geeksforgeeks.org/problems/bit-difference/0

def sol(a, b):
    """
    Take an XOR, so 1 will be set whereever there is bit diff.
    Keep doing AND with the number to check if the last bit is set
    """
    c = a^b
    count=0
    while c:
        if c&1:
            count+=1
        c=c>>1
    return count