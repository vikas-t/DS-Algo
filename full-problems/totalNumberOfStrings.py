#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/total-number-of-strings/0

def sol(n, b, c):
    """
    Naive soln via recursion
    O(1) is (1 + (n * 2) + (n * ((n * n) – 1) // 2))
    """
    if (b < 0 or c < 0): 
        return 0
    if (n == 0) : 
        return 1
    if (b == 0 and c == 0): 
        return 1
 
    return sol(n-1, b, c) + sol(n-1, b-1, c)  + sol(n-1, b, c-1) 


n=5
print(sol(n, 1, 2))