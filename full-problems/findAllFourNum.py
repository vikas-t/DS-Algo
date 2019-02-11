#!/usr/bin/python
# https://practice.geeksforgeeks.org/problems/find-all-four-sum-numbers/0

from functools import cmp_to_key

def compList(a, b):
    for i in range(len(a)):
        if a[i] < b[i]:
            return -1
        else:
            return 1

def getValid(pair1, pair2):
    """
    Validate that the pair does not have the same key used twice
    """
    res = []
    for p1 in pair1:
        for p2 in pair2:
            if not p1 & p2 and p1|p2 not in res:
                res.append(p1|p2)
    return res

def getUnique(arr, res, subRes):
    """
    Check that the sub result does not already exist in the final result and 
    the sub result is sorted
    """
    for rs in subRes:
        x = []
        for i in rs:
            x.append(arr[i])
        if sorted(x) not in res:
            res.append(sorted(x))
    return res
        
def sol(arr, n, k):
    arr.sort()
    m = max(arr)
    h = {}
    for i in range(n-1):
        for j in range(i+1, n):
            p = arr[i]+arr[j]
            if p not in h:
                h[p] = [{i,j}]
            else:
                h[p].append({i,j})
    # Make pairs of two and store their sum in a dictionary with the sum as
    # the key
    
    res = []
    visited = []
    for s in h:
        rem = k - s
        # For every sum check if k-sum exists
        subRes = []
        if {s, rem} in visited:
            continue
        # Lets store a set of sum and remaining sum so as to not 
        # repeat the result - this is not really required and can be skipped
        if rem in h:
            subRes = getValid(h[s], h[rem])
        if subRes:
            res = getUnique(arr, res, subRes)
        visited.append({s, rem})
    
    if res:
        res = sorted(res, key=cmp_to_key(compList))
        for p in res:
            print(" ".join(str(x) for x in p ), end=" $")
    else:
        print(-1, end=" ")

n,k = list(map(int, "27 179".split()))
arr = list(map(int, "88 84 3 51 54 99 32 60 76 68 39 12 26 86 94 39 95 70 34 78 67 1 97 2 17 92 52".split()))
sol(arr, n, k)