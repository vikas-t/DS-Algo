#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/find-the-odd-occurence/0

def sol(arr, n):
    """
    XOR a number with itself, it becomes zero and XOR a number with 0 
    results in the number itself.
    The order does not matter, therefore the odd one gets eliminated out
    EX:  3^3^4^3^3 = 4
    """
    res = 0
    for e in arr:
        res = res^e
    return res