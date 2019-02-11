#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/digit-multiplier/0

def sol(n):
    if n <= 9:
        return n
    
    res = []
    
    for i in range(9, 1, -1):
        while n%i == 0:
            res.append(i)
            n = n//i
    # Keep dividing the number for by digits such that the bigger digit divides
    # it first thereby giving us the smallest possible result
    
    if n > 9:
        return -1
    # If after all divisions we do are not left with a single digit number
    # then the result is not possible
        
    return ''.join(str(x) for x in sorted(res))