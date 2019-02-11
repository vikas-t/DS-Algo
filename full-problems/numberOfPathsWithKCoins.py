#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/number-of-paths-in-a-matrix-with-k-coins/0

def sol(mat, m, n, k, dp):
    """
    Complexity is O(m*n*k)
    """
    if k >= 0 and dp[m][n][k] != None:
        return dp[m][n][k]
    # We have to keep a check so that K does not go out of bounds
    if n == 1 and m == 1 and k == mat[m-1][n-1]:
        return 1
    elif n <= 0 or m <= 0 or k <= 0:
        return 0
    
    dp[m][n][k] = sol(mat, m-1, n, k-mat[m-1][n-1], dp) + sol(mat, m, n-1, k-mat[m-1][n-1], dp)
    return dp[m][n][k]

n = 2
k = 1
arr = [2, 4, 7, 2]
t = 0
mat = [[None for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        mat[i][j] = arr[t]
        t+=1
dp = [[[ None for _ in range(k+1)] for _ in range(n+1)] for _ in range(n+1)]
print(sol(mat, n, n, k, dp))