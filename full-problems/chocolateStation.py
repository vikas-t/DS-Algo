#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/chocolate-station/0

def sol(arr, n, p):
    """
    If we have more chocolates than cost we just pay from the balance
    otherwise we use all the balance and add the remaining to the total
    cost also making bal 0
    """
    bal = 0
    res = 0
    for i in range(n):
        d = arr[i-1]-arr[i] if i > 0 else 0-arr[i]
        # Careful about comparing with arr[-1] when i=0 !!!
        if d > 0:
            bal+=d
        else:
            d = abs(d)
            if bal >= d:
                bal -= d
            else:
                res += d-bal
                bal = 0
                
    return res*p