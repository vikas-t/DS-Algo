#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/subsets/0

from functools import cmp_to_key

def sol(arr, n, N, res, subRes=[]):
    """
    Standard recursive backtracking solution
    """
    if n == N:
        if subRes[:] not in res:
            res.append(subRes[:])
        # Add the subresult to result once we have traversed all the elements
        # in the array
        return
    subRes.append(arr[n])
    sol(arr, n+1, N, res, subRes)
    subRes.pop()
    sol(arr, n+1, N, res, subRes)

def comp(a, b):
    """
    Custom comparator
    """
    for i in range(min(len(a), len(b))):
        if a[i] < b[i]:
            return -1
        elif a[i] > b[i]:
            return 1
    return -1
    # This to handle empty element
            
res = []
arr = [8,1,8,6,8]
arr.sort()
sol(arr, 0, len(arr), res)
#print(res)
print(sorted(res, key=cmp_to_key(comp)))

#()(1)(1 2)(1 2 3)(1 2 3 3)(1 3)(1 3 3)(2)(2 3)(2 3 3)(3)(3 3)
#()(1)(1 6)(1 6 8)(1 6 8 8)(1 6 8 8 8)(1 8)(1 8 8)(1 8 8 8)(6)(6 8)(6 8 8)(6 8 8 8)(8)(8 8)(8 8 8)