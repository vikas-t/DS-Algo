#!/usr/bin/python3
#https://practice.geeksforgeeks.org/problems/geek-and-coffee-shop/0

for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    while m > 1:
    # The loops runs an extra to make the condition false, to rectify that
    # m > 1 is the condition
        n/=2
        m-=1
    print(int(n))