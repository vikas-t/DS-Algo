#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/rotate-a-2d-array-without-using-extra-space/0

def sol(mat, n):
    """
    Read the matrix col wise and invert the values in the rows
    """
    for i in range(n):
        l = 0
        r = n-1
        while l < r:
            mat[i][l], mat[i][r] = mat[i][r], mat[i][l]
            # Keep swapping from left and right and move closer
            l+=1
            r-=1
    
    for i in range(n):
        for j in range(n):
            print(mat[i][j], end=" ")
    print()

# Driver code
for _  in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    mat = [[None for _ in range(n)] for _ in range(n)]
    k=0
    for i in range(n):
        for j in range(n):
            mat[j][i] = arr[k]
            # Read the matrix column wise instead of row wise
            k+=1
    sol(mat, n)