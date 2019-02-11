#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/betting-game/0

def sol(s):
    """
    Update rules as per the statement
    """
    ba = 1
    n = len(s)
    i = 0
    t = 4
    while i < n:
        if t < ba:
            return -1
        if s[i] == "W":
            t = t + ba
            ba = 1
        else:
            t = t - ba
            ba = 2*ba
        i+=1
    return t