#!/usr/bin/python
# https://practice.geeksforgeeks.org/problems/path-in-matrix/0

def sol(arr, n):
    dp = [[0 for j in range(n)] for i in range(n)]
    
    for i in range(n):
        dp[0][i] = arr[0][i]
        
    for i in range(1, n):
        for j in range(n):
            if j == 0:
                dp[i][j] = arr[i][j] +  max(dp[i-1][j], dp[i-1][j+1])
            elif j == n-1:
                dp[i][j] = arr[i][j] + max(dp[i-1][j-1], dp[i-1][j])
            else:
                dp[i][j] = arr[i][j] + max(dp[i-1][j+1], dp[i-1][j-1], dp[i-1][j])

    return max(dp[n-1])