#!/usr/bin/python3

# https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0

def sol(arr, s):
    n = len(arr)
    start = 0
    cur_sum = arr[0]
    i = 0
    while i < n:
        j = start
        while cur_sum > s and j < i:
            cur_sum = cur_sum - arr[j]
            start = start + 1
            j=j+1
        
        if cur_sum == s:
            return start, i
        
        i+=1
        if i<n:
            cur_sum = cur_sum + arr[i]
    return False

print(sol([1,2,3,7,5], 12))