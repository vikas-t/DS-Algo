#!/usr/bin/python

# https://practice.geeksforgeeks.org/problems/word-break/0

def sol(s, words):
    if len(s) == 0:
        return 1
    for i in range(1,len(s)+1):
        if s[:i] in words and sol(s[i:], words) == 1:
            return 1
    return 0

