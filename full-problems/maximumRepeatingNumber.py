#!/usr/bin/python3
#https://practice.geeksforgeeks.org/problems/maximum-repeating-number/0

for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    for i in range(n):
        arr[arr[i]%k] += k
    # This is basically saying - using the value of elements as index keep
    # keep adding k to it so if arr[i] = 3, make it arr[3] = arr[3] + k
    for i in range(n):
        arr[i]-=arr[i]%k
    # Subtract the remaindr
    # ??, original solution not mine
    m = arr[0]
    mi = 0
    for i in range(n):
        if arr[i] > m:
            m = arr[i]
            mi = i
    print(mi)