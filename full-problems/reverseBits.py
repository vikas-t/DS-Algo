#!/usr/bin/python3
#https://practice.geeksforgeeks.org/problems/reverse-bits/0

def sol(n):
    """
    Get the last bit and build the number treating it as first from the left
    and so on..
    """
    p = 31
    res = 0
    while p >= 0:
        bit = n&1
        res = res + bit*(1<<p)
        # 1<<p is like saying 2**p
        p-=1
        n=n>>1
    return res
print(sol(1))

# https://www.geeksforgeeks.org/reverse-bits-using-lookup-table-in-o1-time/
# soln in O(1) time