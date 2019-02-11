#!/usr/bin/python3
#https://practice.geeksforgeeks.org/problems/count-total-set-bits/0

def sol(n):
    i = 0    
    res = 0
    while (1 << i) <= n:
        # i keeps a check of total number of bits required to form n
        c = 1 << i
        k = 0
        for _ in range(n+1):
        # For every number till n count the ith bit which alternates 
        # after every 2^i, c keeps a check on the change and k is the bit
            res += k 
            if c == 1:
                k = int(not k)
                c = 1 << i
            else:
                c-=1
        i+=1
    return res