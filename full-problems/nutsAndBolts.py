#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/nuts-and-bolts-problem/0

def sol(nuts, bolts, n):
    """
    For the given order if nuts and bolts print both !!
    Strange question !
    """
    types = ["!",  "#",  "$",  "%",  "&",  "*",  "@" , "^", "~"]
    for t in types:
        if t in nuts and t in bolts:
            print(t, end=" ")
    print()
    for t in types:
        if t in nuts and t in bolts:
            print(t, end=" ")
    print()