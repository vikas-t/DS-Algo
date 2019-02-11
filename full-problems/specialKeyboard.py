#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/special-keyboard/0

def sol(n):
    """
    b is the break point after which only one ctrl+c and ctrl+v will
    happen and the remaining will be all ctrl+v therefore it starts at the 
    end from n-3
    Now, say if b is the break point then n-b is left on the right side,
    of which 2 strokes will be consumed in select and copy, and the remaining
    will be used for pasting i.e n-b-2 times the sub result(which is sol(b)) 
    on the left will pasted. So left side gives you 1.
    Total becomes n-b-2+1 = n-b-1 
    """
    if n <= 6:
        return n
    
    mx = 0
    for b in range(n-3, 0, -1):
        m = sol(b)*(n-b-1)
        mx = max(mx, m)
    return mx

def dpSol(n):
    dp = [0]*(n+1)
    for i in range(1, 7):
        dp[i] = i
    
    for i in range(7, n+1):
        for b in range(i-3, 0, -1):
            dp[i] = max(dp[i], dp[b]*(i-b-1))
    
    return dp[n]

print(dpSol(7))

