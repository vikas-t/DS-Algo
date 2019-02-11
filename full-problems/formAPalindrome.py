#!/usr/bin/python
# https://practice.geeksforgeeks.org/problems/form-a-palindrome/0


def sol(s):
    """
    Consider a string 'ABCD'
    A. If the last character is same as the first one than the problem reduces
    by one length from both the ends 
    ----> sol(l, h) => sol(l+1, h-1)
    If statement A is not true, there are two ways to break it in to a
    subproblems
    1. We insert a character at the start 'DABCD', so now first and last
       characters are equal and problem reduces by one length from the end.
       Effectively, sol(l, h) => sol(l, h-1)
    2. We insert a character at the end 'ABCDA' to rule out first and last
       characters reducing the problem by one length
       so, sol(l, h) => sol(l+1, h)
    We take the minimum of both these
    
    In the dynamic approach, we have to fill the table diagonally
    """
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    for length in range(1, n):
        l = 0
        h = length + l
        while h < n:
            if s[l] == s[h]:
                dp[l][h] = dp[l+1][h-1]
            else:
                dp[l][h] = 1 + min(dp[l][h-1], dp[l+1][h])
            l+=1
            h+=1
    return dp[0][n-1]