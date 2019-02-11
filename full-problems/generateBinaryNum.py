#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/generate-binary-numbers/0

def sol(n):
    """
    Generates binary number from 1 to n and prints it
    """
    q = []
    q.append('1')
    
    for i in range(n):
        res = q.pop(0)
        print(res, end=" ")
        q.append(res+'0')
        q.append(res+'1')
    print()