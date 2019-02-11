#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/save-knights/0

import math

def sol(n):
    """
    Not very sure how it works. Wrapping up
    """
    if n == 2: return 4
    return math.ceil(n*n/2)