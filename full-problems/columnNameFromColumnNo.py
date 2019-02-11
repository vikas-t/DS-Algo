#!/usr/bin/python

# https://practice.geeksforgeeks.org/problems/column-name-from-a-given-column-number/0

def sol(num):
    d = 'ZABCDEFGHIJKLMNOPQRSTUVWXY'
    res = ''
    while num>0 :
        r = num%26
        res += d[r]
        num=num//26
        if r == 0: 
            num = num - 1
        # When the remainder is 1 it is 'A' when it is 2 it is 'B' when it
        # reaches 26 it is 'Z' but because it divides it, the quotient 
        # increases by 1. So while converting it backwards we decrease the 
        # quotient by 1 to make it compensate
        # In other words  we are considering 26 to be ‘Z’ while in 
        # actual it’s 25th with respect to ‘A’.
    return res[::-1]