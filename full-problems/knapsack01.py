#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem/0

def sol(n, w, wt, v):
    dp = [[0 for _ in range(w+1)]for _ in range(n+1)]
    
    for i in range(n+1):
        for j in range(w+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            # If either there are no items or max wt capacity is 0
            # We cannot pick anything so 0
            elif wt[i-1] <= j:
                dp[i][j] = max(v[i-1] + dp[i-1][j-wt[i-1]], dp[i-1][j])
            # If the item can be picked, then take the max when chosing
            # it and when not chosing it
            else:
                dp[i][j] = dp[i-1][j]
            # Item cannnot be picked, we reduce the number of items
    return dp[n][w]