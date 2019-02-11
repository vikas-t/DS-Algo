#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/number-of-1s-in-smallest-repunits/0

def sol(n):
    """
    Approach 1:
    1. We try the division for 1, 11, 111, 1111.... till we get the remainder
       0, This is not very efficient and the number will become too large
    2. Next approach is, we dont want to know the number we will check for the
       remainder which is 0 and we keep counting the digits.
       We use the follwing property:  If a number say n, leaves the remainder
       r when divided with another number. Then adding or subtracting anything
       to n would leave the same remainder as adding and substracting anything
       t0 r.
       For ex: 40%9 = 4
       Next, (40+25)%9 = 2
       Also  (4+25)%9 = 2
       
       Similarily,
       38%7 = 3
       (38*19)%7 = 1
       (3*9)%7 = 1
    """
    r = 1
    # Let the first no. be 1
    c=1
    
    while r:
        r = (10*r+1)%n
        # The next no. is 10*n+1 and thus the next remainder is 10*r+1 and
        # we do this till we find the remainder 0
        c+=1
    return c
