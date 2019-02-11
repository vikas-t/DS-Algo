#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/maximum-product-of-two-numbers/0

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    m1 = -1
    m2 = -1
    # Because the numbers are > 0, we can initialise with -1
    for x in arr:
        if x > m1:
            m2 = m1
            m1 = x
        elif x > m2:
            m2 = x
    # There are atleast two numbers in the array
    print(m1*m2)
