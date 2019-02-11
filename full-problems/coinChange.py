#!/usr/bin/python

# The standard coin change problem

def dpCoinChange(arr, m, n):
    dp = []
    
    for i in xrange(n+1):
        dp.append([])
        for j in xrange(m):
            dp[i].append(0)
            if i == 0:
                dp[i][j] = 1
    
    for i in xrange(1, n+1):
        for j in xrange(m):
            x = dp[i-arr[j]][j] if i-arr[j] >= 0 else 0
            y = dp[i][j-1] if j >=1 else 0
            dp[i][j] = x + y
    return dp[n][m-1]

def dpCoinChange2(arr, n, v):
    # Same solution written in a slightly diff way
    dp = [[0 for j in range(v+1)] for i  in range(n)]
    
    for i in range(n):
        dp[i][0] = 1
    
    for i in range(n):
        for j in range(1, v+1):
            x = dp[i][j - arr[i]] if j-arr[i] >= 0 else 0
            y = dp[i-1][j] if i-1 >= 0 else 0
            dp[i][j] = x + y
    return dp[n-1][v]

arr = [1,2,3]
len(arr)
v = 4

print dpCoinChange(arr, len(arr), v)
print dpCoinChange2(arr, len(arr), v)