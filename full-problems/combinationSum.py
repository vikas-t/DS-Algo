#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/combination-sum/0

from functools import cmp_to_key

def comp(a, b):
    for i in range(min(len(a), len(b))):
        if a[i] < b[i]:
            return -1
        if a[i] > b[i]:
            return 1
    
def printSol(result):
    for sr in sorted(result, key=cmp_to_key(comp)):
        print("(" + " ".join(str(x) for x in sr) + ")", end="")
    print()
    
def sol(arr, n, t, subRes=[]):
    if t == 0:
        subRes = sorted(subRes)
        if subRes not in res:
            res.append(sorted(subRes[:]))
    
    if n == 0 or t < 0:
        return
    
    if arr[n-1] <= t:
        tc = t
        for i in range(t//arr[n-1]):
            subRes.append(arr[n-1])
            tc = tc - arr[n-1]
            sol(arr, n-1, tc, subRes)
    # We divide the number by the total to know how many times the number can be included
    # This way we do not have to check the inclusion of the number for the every other
    # number in the rest of the set. This improves the efficiency
        
        for i in range(t//arr[n-1]):
            subRes.pop()
        # Remove all inclusions of the number
        
    sol(arr, n-1, t, subRes)
    
    
r = []    
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    t = int(input())
    res = r[:]
    sol(arr, n, t)
    if not res:
        print("Empty")
    else:
        printSol(res)
