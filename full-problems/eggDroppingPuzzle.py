#!/usr/bin/python
# https://practice.geeksforgeeks.org/problems/egg-dropping-puzzle/0

import sys

def sol(n, k):
    dp = [[sys.maxsize for j in range(k+1)] for i in range(n+1)]
    
    for i in range(1, n+1):
        dp[i][0] = 0
        dp[i][1] = 1
        # For 0 floors result is 0
        # For 1 floor result is 1
    
    for i in range(1, k+1):
        dp[1][i] = i
        # If there is only one egg, it requires k dropping
    
    for i in range(2, n+1):
        for j in range(2, k+1):
            for x in range(1, j+1):
                res = 1 + max(dp[i-1][x-1], dp[i][j-x])
                # We take max as we want the worst case
                dp[i][j] = min(dp[i][j], res)
    
    return dp[n][k]
