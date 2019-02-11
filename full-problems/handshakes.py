#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/handshakes/0

def sol(n, mem):
    """
    Every handshake divides the circle in to two more circles and so on.
    Let n = 8
    So if a 5 shakes hand with 8 (5->6->7->8) it is 4th counting from 5 so
    i = 4, the circle gets divides in to the following 
    i-2 = 2(6->7) 
    n-i = 4 = (1->2->3->4)
    We memoize the solution for performance
    """
    if mem[n] != -1:
        return mem[n]
    
    mem[n] = 0
    for i in range(2, n+1):
        mem[n]+=sol(n-i, mem)*sol(i-2, mem)
        
    return mem[n]

for _ in range(int(input())):
    n = int(input())
    mem = [-1]*(n+1)
    # To memoize
    mem[0] = 1
    print(sol(n, mem))