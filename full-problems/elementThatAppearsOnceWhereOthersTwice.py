#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/element-that-appears-once-where-every-element-occurs-twice/0

# XOR of any number with 0 results in the same number
# XOR of number with same number results in 'Zero'
# So if we take the XOR of all elements the one doubles will zero out and 
# only the single number will remain
def sol(arr, n):
    res = arr[0]
    # We have started with 2nd element but res can be zero and we can start
    # with the first element
    for i in range(1, n):
        res=arr[i]^res
    res