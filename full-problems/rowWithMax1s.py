#!/usr/bin/python3
# https://www.geeksforgeeks.org/find-the-row-with-maximum-number-1s/


def sol(mat, m, n):
    """
    Traverse column from the end if 1 is the value increase counter
    else switch to next row
    """
    c = 0
    j = n-1
    i = 0
    while i < m and j > -1:
        if mat[i][j] == 1:
            c = i
            j-=1
        else:
            i+=1
    return c