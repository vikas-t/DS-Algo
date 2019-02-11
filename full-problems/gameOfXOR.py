#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/game-of-xor/0

def sol(arr, n):
    """
    If the array is 3,5,2,1
    Following are the subarrays
    (3), (3,5), (3,5,2), (3,5,2,1) - 3 occurs 4 times
    (5), (5, 2), (5,2,1) - 5 is 3 times
    (2), (2, 1) - 2 twice
    (1) - once
    It can be deduced that element at ith position will have its frequency
    n-i*(i+1). We care for only odd frequencies as the even frequency
    will be zeroed out and off the odd frequencies only the number will remain
    so we include that number in the result
    """
    res = 0
    for i in range(n):
        f = (n-i)*(i+1)
        if f % 2 != 0:
            res = res^arr[i]
    return res