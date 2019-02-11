#!/usr/bin/python3
# https://www.geeksforgeeks.org/dice-throw-dp-30/

def sol(m, n, x):
    """
    The bruteforce recursive solution
    """
    if x == 0 and n == 0:
        return 1
    elif n < 0 or x < 0:
        return 0
    # It is given in the question that X is the summation of all values on
    # each faces, so we accept the solution(return 1) only when the 
    # Sum is zero and the no. of throws left are zero
    # For all the other cases we return 0
    
    res = 0
    for i in range(1, m+1):
        res += sol(m, n-1, x-i)
    # Try every m and recurse 
    
    return res

def dp(m, n, x):
    """
    The bottom up dynamic programing approach
    """
    dp = [[0 for _ in range(x+1)] for _ in range(n+1)]
    
    dp[0][0] = 1
    # Only when the no. of throw are zero and Sum is 0, the no. of ways are 1
    # else the number of ways are 0
    
    for i in range(1, n+1):
        for j in range(1, x+1):
            for k in range(1, m+1):
                if j-k >= 0:
                    dp[i][j] += dp[i-1][j-k]
    
    return dp[n][x]

print(sol(6, 3, 12))
print(sol(10, 8, 25))
print(dp(6, 3, 12))
print(dp(10, 8, 25))