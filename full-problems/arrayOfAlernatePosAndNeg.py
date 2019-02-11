#!/usr/bin/python
#https://practice.geeksforgeeks.org/problems/array-of-alternate-ve-and-ve-nos/0
def sol(arr):
    """
    Create two lists of positives and negatives and print taking one from
    each. Print the remaining array
    Careful about 0
    """
    p = []
    n = []
    for x in arr:
        if x < 0:
            n.append(x)
        else:
            p.append(x)
    mn = min(len(p), len(n))
    for i in range(mn):
        print(p[i], n[i], end=" ")
    
    for i in range(mn, len(p)):
        print(p[i], end=" ")
    
    for i in range(mn, len(n)):
        print(n[i], end=" ")
    print()
