#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/sum-equals-to-sum/0

def sol(arr, n):
    """
    For every sum of two elements store it in a hash where 'sum' is the key
    and list of sorted indexes are values. If for a given sum the indexes
    do not already exist return True
    """
    sh = {}
    for i in range(n-1):
        for j in range(i+1, n):
            s = arr[i]+arr[j]
            k = sorted((i, j))
            if s in sh and k not in sh[s]:
                return 1
            else:
                sh[s] = [k]
    return 0