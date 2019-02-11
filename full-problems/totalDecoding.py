#!/usr/bin/python

#https://practice.geeksforgeeks.org/problems/total-decoding-messages/0
#code

def validate(s):
    if s[0] == '0':
        return False
    
    if '00' in s:
        return False
    
    return True


def sol(arr, n):
    if not validate(arr):
        return 0
    
    dp = [0]*(n+1)

    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = 0
        if arr[i-1] > '0':
            dp[i] = dp[i-1]
        
        if arr[i-2] == '1' or (arr[i-2] == '2' and arr[i-1] <='6'): 
                dp[i] += dp[i-2]
    return dp[n]