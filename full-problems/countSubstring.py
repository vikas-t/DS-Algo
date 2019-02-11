#!/usr/bin/python3
#https://practice.geeksforgeeks.org/problems/count-substrings/0

def sol(s):
    """
    Count the no. of 1s. Start and end can be any 1. So soln is combination
    of nC2 which is n*(n-1)//2*1
    """
    c = 0
    for x in s:
        if x == '1':
            c+=1
    return (c*(c-1))//2