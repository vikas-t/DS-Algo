#!/usr/bin/python3
import sys

def kadane(arr):
    mx = -1*sys.maxsize
    mi = -1*sys.maxsize
    mth = 0
    for x in arr:
        mth += x
        mth = max(0, mth)
        mx = max(mth, mx)
        mi = max(mi, x)
        # To handle if all the numbers are non negative
    return mi if mx == 0 else mx

def sol(arr, m, n):
    """
    Fixing the left and right columns, create a aux array that contains all 
    the values row wise and apply kadane on the aux array. Kadane will return
    the max sum (of a subrray) in the row and this way we can fix the top
    row and col. Complexity is n^3
    Another approach to understanding is pick any two  columns and fold it 
    in the plane to make a 1d array thereby adding all elements of the same
    row together. Now apply kadane on the 1d array
    """
    mx = -1*sys.maxsize
    for l in range(n):
        tmp = [0]*(m)
        # Aux array of row length
        for r in range(l, n):
            for i in range(m):
                tmp[i] += arr[i][r]
                # Add up the values in the rows, to create a 1d array
            s = kadane(tmp)
            print(tmp, s)
            mx = max(s, mx)
    return mx

arr = [1, 2, -1, -4, -20, -8, -3, 4, 2, 1, 3, 8, 10, 1, 3, -4, -1, 1, 7, -6]
m, n = 4, 5
mat = [[None for _  in range(n)] for _ in range(m)]
k = 0
for i in range(m):
    for j in range(n):
        mat[i][j] = arr[k]
        k+=1 
print(sol(mat, 4, 5))