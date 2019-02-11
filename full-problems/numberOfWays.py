#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/number-of-ways/0

def sol(n):
    """
    Standard DP problem
    The width is 4 always, so we need to worry only about the length 
    which can be reduced either by 1 or by 4 i.e keeping the tile 
    horizontally or vertically
    """
    dp = [0]*(n+1)
    if n < 4:
        return 1
    dp[0] = 1 # If the length is 0, there is no solution which is one way
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-4]
    return dp[n]