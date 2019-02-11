#!/usr/bin/python
# https://practice.geeksforgeeks.org/problems/count-ways-to-reach-the-nth-stair/0

def cal():
    """
    Trick is to calculate all in one go for the given limit of n
    """
    dp = [0 for i in range(100001)]
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, 100001):
        dp[i] = (dp[i-1] + dp[i-2])%1000000007
    return dp