#!/usr/bin/python

#https://practice.geeksforgeeks.org/problems/maximum-sum-increasing-subsequence/0

def sol(arr, n):
    dp = [arr[i] for i in range(n)]
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+arr[i])
    return max(dp)