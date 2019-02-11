#!/usr/bin/python

# https://practice.geeksforgeeks.org/problems/stickler-theif/0

def sol(arr):
    n = len(arr)
    dp = [0]*(n+1)
    dp[0] = 0
    if n > 0:
        dp[1] = arr[0]
    if n > 1:
        dp[2] = max(arr[0], arr[1])
    
    for i in range(3, n+1):
        dp[i] = max(dp[i-1], dp[i-2]+arr[i-1])
    
    return dp[n]
    

def sol2(arr):
    n = len(arr)
    if n==0: return 0
    
    a = arr[0]
    if n == 1: return a
    
    b = max(arr[0], arr[1])
    if n == 2: return b
    
    mv = None
    for i in range(2, n):
        mv = max(b, a + arr[i])
        a = b
        b = mv
    
    return mv

print sol2([5, 5, 10, 100, 10, 5])