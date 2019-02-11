#!/usr/bin/python
#https://practice.geeksforgeeks.org/problems/is-binary-number-multiple-of-3/0

def sol(x):
    """
    If the diff. of even set bits and odd set bits is divisible by 3, then
    the number is divisible by 3
    """
    n = len(x)
    oddCount = 0
    evenCount = 0
    
    for i in range(n):
        if i%2 == 0:
            if x[i] == '1':
                evenCount += 1
        else:
            if x[i] == '1':
                oddCount += 1
    
    if abs(evenCount-oddCount)%3 == 0:
        return 1
    return 0