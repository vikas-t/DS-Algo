#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/how-many-xs/0

def getDigCount(num, n):
    c = 0
    while num>0:
        #print(num)
        if num%10 == n:
            c+=1
        num=num//10 #careful here saying num/10
    return c
    
def sol(n, l, r):
    """
    Count all digits for all given numbers
    Another approach is to convert it to string and count the characters
    as digits
    """
    c=0
    for i in range(l+1, r):
        c+=getDigCount(i, n)
    return c