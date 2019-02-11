#!/usr/bin/python

# https://practice.geeksforgeeks.org/problems/four-elements/0

def validPair(pair1, pair2):
    """
    Validates that the sets have nothing in common or the pair is unique
    """
    for p1 in pair1:
        for p2 in pair2:
            if not p1 & p2:
                return True
    return False
        
def sol(arr, n, k):
    """
    Create a hash of all possible two element sums.
    For every element (say p) in the hash check if k-p is in the hash 
    and the elements are unique 
    """
    m = max(arr)
    c = [[] for i in range(2*m+1)]
    # Use list comprehension instead of saying [[]]*(2*m+1)
    for i in range(n-1):
        for j in range(i+1, n):
            s = arr[i]+arr[j]
            c[s].append({i,j})
            # For every sum we store the set of all possible i and j in a set
            
    for p in range(len(c)):
        if not c[p]:
            continue
        q = k - p
        if q >= 0 and q < len(c) and c[q] and validPair(c[p], c[q]):
           return 1
    return 0