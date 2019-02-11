#!/usr/bin/python

# https://practice.geeksforgeeks.org/problems/check-if-string-is-rotated-by-two-places/0

def sol(s, rs):
    """
    Check if at any place the difference b/w the characters is non zero
    """
    if len(s) != len(rs):
        return False
    n = len(s)
    for i in range(len(s)):
        if ord(s[i]) - ord(rs[(i+2)%n]) != 0 and ord(rs[i]) - ord(s[(i+2)%n]) != 0:
            return False
    return True