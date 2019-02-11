#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/magic-number/0

def sol(n):
    """
    If we notice carefully the magic numbers can be represented 
    as 001, 010, 011, 100, 101, 110 etc, where 001 is 
    0*pow(5,3) + 0*pow(5,2) + 1*pow(5,1). So basically we need to 
    add powers of 5 for each bit set in given integer n.
    """
    p = 1
    res = 0
    
    while n:
        p*=5
        if n&1:
            res+=p
        n=n>>1
    return res%1000000007
    