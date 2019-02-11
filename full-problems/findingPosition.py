#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/finding-position/0

def sol(n):
    """
    Every time the queue is reduced to half the length so it will take 
    logn to reduce it to 1. So the last power of 2 is the soln
    """
    for i in range(n, 0, -1):
        if i&(i-1) == 0:
            return i