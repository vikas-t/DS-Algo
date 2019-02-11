#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/game-with-string/0

import heapq

def sol(s, k):    
    """
    Keep decreasing the max frequency by 1 uptill k.
    We store the frequencies in a max heap to get the max each time
    """
    f = [0]*26
    for x in s:
        f[ord(x)-97] -= 1
    # We store the negative of the frequencies
     
    heapq.heapify(f)
    # Make it a max heap
    
    while k and f:
        d = heapq.heappop(f)
        heapq.heappush(f, d+1)
        # Reduce the max frequency by 1 and k by 1 till k exists
        k-=1
    
    res = 0
    for x in f:
        res += x**2
    # Return the result, we dont care for the '-' since its gets squared
    return res