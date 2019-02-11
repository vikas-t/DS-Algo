#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/combination-sum-part-2/0

res = []

from functools import cmp_to_key

def comp(a, b):
    for i in range(min(len(a), len(b))):
        if a[i] < b[i]:
            return -1
        if a[i] > b[i]:
            return 1

def recSol(arr, n, t, subRes=[]):
    #print("n="+str(n), "t="+str(t), subRes)
    if t == 0:
        subRes = sorted(subRes)
        if subRes not in res:
            res.append(subRes[:])
    if n == 0:
        return
    if arr[n-1] <= t:
        subRes.append(arr[n-1])
        recSol(arr, n-1, t-arr[n-1], subRes)
        subRes.pop()
        recSol(arr, n-1, t, subRes)
    else:
        recSol(arr, n-1, t, subRes)
        
arr = [10, 1, 2, 7, 6, 1, 5]
t = 8
recSol(arr, len(arr), t)
print(sorted(res, key=cmp_to_key(comp)))