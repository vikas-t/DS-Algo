#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room/0

from functools import cmp_to_key

def comp(a, b):
    """
    Sort the meetings by Finishing time
    """
    if a[1] < b[1]:
        return -1
    elif a[1] == b[1] and a[0] > b[0]:
        # If two meetings finish at the same time, pick the smaller one
        return -1
    else:
        return 1

def sol(s, f, n):
    # Greedy approach pick the one that finishes first or the smaller one
    # if they finish at the same time
    ms = []
    for i in range(n):
        ms.append((s[i], f[i], i+1))
    # Let meeting be represented by tuple and the last element is used to store
    # the original order of the meeting. Add 1 as the index starts from 1
    
    ms = sorted(ms, key=cmp_to_key(comp))
    #print(ms)
    le = 0
    for i in range(len(ms)):
        if ms[i][0] > le:
            print(ms[i][2], end=" ")
            le = ms[i][1]
    print()