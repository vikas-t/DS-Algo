#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/single-number/0

def sol(arr, n):
    """
    The usual XOR approach
    """
    res = 0
    for i in range(n):
        res = res^arr[i]
    return res