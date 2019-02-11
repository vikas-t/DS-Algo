#!/usr/bin/python3
#https://practice.geeksforgeeks.org/problems/product-array-puzzle/0

def sol(arr, n):
    p = 1
    for x in arr:
        p*=x
    
    for x in arr:
        print(p//x, end=" ")
    print()
