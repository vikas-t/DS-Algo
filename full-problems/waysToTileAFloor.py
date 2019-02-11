#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/ways-to-tile-a-floor/0
def sol(n):
    """
    The breadth which is two can be covered by only two ways we either keep
    a 2*1 tile or two 1*2 tiles. No other arrangement is possible. So we have
    two ways to cover the length W, either reduce it by 2 or reduce it by 1
    In other words its a fibonacci series
    """
    if n == 0 or n == 1:
        return 1
        
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]