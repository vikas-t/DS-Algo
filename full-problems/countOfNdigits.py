#!/usr/bin/python

#https://practice.geeksforgeeks.org/problems/count-of-n-digit-numbers-whose-sum-of-digits-equals-to-given-sum/0

def solP(s, n, res=[]):
    """
    This prints the solution
    """
    if n == 0 and s == 0:
        print(res[:])
        return
    elif n < 0 or s <= 0:
        return 0
    
    for i in range(10):
        if i <= s:
            res.append(i)
            sol(s-i, n-1, res)
            res.pop()

def sol(s, n, lookup):
    """
    This counts the no. of solutions. To reduce the complexity we have used
    a lookup table.
    """
    #print(lookup)
    if lookup[s][n] != None:
        return lookup[s][n]

    if n == 0 and s == 0:
        return 1
    # Leading zeroes are not counted because in that case s will be zero
    # before n becomes zero
    elif n < 0 or s <= 0:
        return 0

    c = 0
    for i in range(10):
        if i <= s:
            c += sol(s-i, n-1, lookup)
            lookup[s][n] = c%1000000007
    return lookup[s][n]

n = 94
s = 336
lookup = [[None for _ in range(n+1)]for _ in range(s+1)]
print(sol(s, n, lookup))