#!/usr/bin/python

# https://practice.geeksforgeeks.org/problems/equal-to-product/0

def sol(arr, n, p):
    """
    Space complexity: O(1)
    Time complexity: O(nlogn)
    """
    arr.sort()
    l = 0
    r = n-1
    while r >= 0 and l < r and l < n:
        if arr[l]*arr[r] == p:
            return True
        elif arr[l]*arr[r] > p:
            r=r-1
        else:
            l=l+1
    return False

def sol2(arr, n, p):
    """
    Space complexity: O(k) k is max ele. in array
    Time comlexity: O(n)
    """
    m = max(arr)
    c = [0]*(m+1)
    for e in arr:
        c[e]+=1
    
    for e in arr:
        if p%e==0:
            q = p//e
            if e == q and c[e] > 1:
                return True
            elif q < m+1 and c[q] > 0: 
                return True
    return False

arr = [674, 665, 142, 712, 254, 869, 548, 645, 663, 758, 38, 860, 724, 742, 530, 779, 317, 36, 191, 843, 289, 107, 41, 943, 265, 649, 447, 806, 891, 730, 371, 351, 7, 102]
print(sol(arr, len(arr), 115928))