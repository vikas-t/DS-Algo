#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/maximum-money/0

def sol(n, m):
    if n == 1:
        return m
    if n%2 == 0:
        return n//2*m
    else:
        return (n//2+1)*m