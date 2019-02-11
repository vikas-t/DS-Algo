#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/save-knights/0

import math

def sol(n):
    """
    knight, when on a black square, can only attack white squares. 
    Likewise, a knight on a white square can only attack black squares. 
    That means that if you only place your knights on the same colour 
    squares on the board they will not attack one another.
    So, lets say n = 5. Total squares = 25. 13 will be of one color, 12 of the
    other. We take the bigger one
    """
    if n == 2: return 4
    return math.ceil(n*n/2)