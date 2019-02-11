#!/usr/bin/python

#https://practice.geeksforgeeks.org/problems/number-of-coins/0

import sys

def sol(arr, n, v):
    """
    If V == 0, then 0 coins required.
    If V > 0
    minCoin(coins[0..m-1], V) = min {1 + minCoins(V-coin[i])} 
                               where i varies from 0 to m-1 
                               and coin[i] <= V 
    """
    dp = [sys.maxsize for i in range(v+1)]
    # No 2d array is required here because we need not track coins
    
    dp[0] = 0
    
    for i in range(1, v+1):
        for j in range(n):
            if arr[j] <= i:
                x = dp[i-arr[j]]
                if x != sys.maxsize and x+1 < dp[i]:
                    dp[i] = x+1
                    
    if dp[v] != sys.maxsize:
        return dp[v]
    return -1

print(sol([3], 1, 8))