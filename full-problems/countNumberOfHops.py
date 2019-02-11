#!/usr/bin//python3
# https://practice.geeksforgeeks.org/problems/count-number-of-hops/0
def sol(n):
    if n <= 1:
        return 1
    if n == 2:
        return 2

    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[n]