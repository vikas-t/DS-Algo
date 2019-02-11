#!/usr/bin/python3

# Longest increasing subsequence

import sys 

def longer_list(list1, list2):
    if len(list1) > len(list2):
        return list1
    else:
        return list2

def lis_rec(list, last=-1*sys.maxint):
    """
    Recursive solution that prints the list
    """
    if not(list):
        return []
   
    incl = []
    if list[0] > last:
        incl = [list[0]] + lis_rec(list[1:], list[0])   
    excl = lis_rec(list[1:], last)

    return longer_list(incl, excl)

def listRec(arr, n, cur=0, prev=None):
    if cur >= n:
        return 0
    
    incl = 0
    excl = 0
    if prev == None or arr[cur] > arr[prev]:
        incl = 1 + listRec(arr, n, cur+1, cur)
    excl = listRec(arr, n, cur+1, prev)
    
    return max(incl, excl)

def lis_dp(arr):
    """
    Best solution
    """
    n = len(arr)
    dp = [1]*n
    for i in range(n):
        for j in range(i):
            if arr[j] <= arr[i]:
            # Watch out if = is not needed
                dp[i] = max(dp[i], dp[j]+1)
                # Max of included or excluded
    return max(dp)
    # dp can also be empty, you can return 0 in that case
    # Return the longest

test_cases = [
   [1, 10, 2, 11, 12],
   [15],
   [1, 2],
   [10, 2, 3, 19, 21, 90],
   [5, 4, 3, 2],
   [1, 2, 3, 4, 5, 6],
   [1, 15, 19, 2, 7, 14],
   [5,6, 7, 2, 3],
   [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
]

# Driver code

for case_list in test_cases:
    print lis_dp(case_list), listRec(case_list, len(case_list))
    # Compare both solutions