#!/usr/bin/python3
#https://practice.geeksforgeeks.org/problems/minimum-sum-partition/0

def sol(arr, n):
    s = sum(arr)
    dp = [[False for _ in range(n+1)] for _ in range(s+1)]
    
    for i in range(n+1):
        dp[0][i] = True
    # The sum 0 is possible excluding all elements
    
    for i in range(1, s+1):
        dp[i][0] = False
    # If there are no elements, any sum except
    # 0 is not possible
    
    for i in range(1, s+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i][j-1]
            # Excluding the element
            dp[i][j] = dp[i][j] or dp[i-arr[j-1]][j-1]
    
    for i in range(s//2, -1, -1):
    # The closest to s/2 will give the min diff as the sum of the other 
    # half of the array would also approach s/2
        if dp[i][n]:
            d = s - 2*i
            return d