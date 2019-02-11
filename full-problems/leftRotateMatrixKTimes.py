#!/usr/bin/python3
#https://practice.geeksforgeeks.org/problems/left-rotate-matrix-k-times/0

def sol(arr, m, n, k):
    res = [[None for _ in range(n)] for _ in range(m)]
    # Create auxiliary array to store the result
    
    for i in range(m):
        for j in range(n):
            if j >= k:
                res[i][j-k] = arr[i][j]
            else:
                res[i][n+j-k] = arr[i][j]
        # If rotation is 2 to the left then 1 has to become n-1 which is 
        # basically saying n+(1-2)
    
    for i in range(m):
        for j in range(n):
            print(res[i][j], end=" ")