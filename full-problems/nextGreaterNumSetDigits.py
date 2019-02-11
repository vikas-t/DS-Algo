#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/next-greater-number-set-digits/0

import sys

def sol(num):
    arr = [int(x) for x in str(num)]
    n = len(arr)
    
    found = False
    for i in range(n-1, 0, -1):
        if arr[i-1] < arr[i]:
            li = i-1
            found = True
            break
    # Remember a sorted number has its digits in descending order  and
    # a reverse sorted in ascending number
    # Find the first digits from the end which is greater than its previous
    # digit, if we dont find such digits meaning the number is sorted in
    # reverse and is the highest, so we return -1
    # Once we found the digit, we need to find a digit to its right which
    # is next greater(or min diff b/w the digits)
    # We swap those digits and sort the rest of the array
    
    if not found:
        return False
    
    md = sys.maxsize
    mi = None
    for i in range(li+1, n):
        if arr[i] > arr[li] and arr[i] - arr[li] < md:
            # Careful with zeroes
            md = arr[i] - arr[li]
            mi = i
    
    arr[li], arr[mi] = arr[mi], arr[li]
    
    res = []
    res = arr[:li+1] + sorted(arr[li+1:])
    return ''.join(str(i) for i in res)