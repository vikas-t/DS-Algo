#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/reverse-each-word-in-a-given-string/0

for _ in range(int(input())):
    arr = list(input().split("."))
    n = len(arr)
    for i in range(n-1):
        print(arr[i][::-1], end=".")
    print(arr[n-1][::-1])