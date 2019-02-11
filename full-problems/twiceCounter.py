#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/twice-counter/0

def sol(words):
    h = {}
    res = 0
    for word in words:
        h[word] = h[word] + 1 if word in h else 1
    for word in h:
        if h[word] == 2:
            res+=1
    return res