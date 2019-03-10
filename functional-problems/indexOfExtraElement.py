#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/index-of-an-extra-element/1

def findExtra(a,b,n):
    """
    Both arrays are sorted so we return the first point of inequality
    """
    i = 0
    na = len(a)
    nb = len(b)
    
    while i < na and i < nb and a[i] == b[i]:
        i+=1
    return i