#!/usr/bin/python3
#https://practice.geeksforgeeks.org/problems/check-if-a-number-can-be-expressed-as-xy/0

def sol(n):
    if n <= 1:
        return True
    for i in range(2, int(n**0.5)+1):
        j = i
        while j <= n:
            j = j*i
            if j == n:
                return True
    return False

print(sol(84))