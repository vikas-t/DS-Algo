#!/usr/bin/python

# Return largest subsequence of the same letter

def maxLen(a, b):
    if len(a) > len(b):
        return a
    return b

def recSol(s):
    n = len(s)
    if n == 1:
        return s[n-1]
    f = s[0]
    subr = recSol(s[1:])
    if subr[0] == f:
        return f+subr
    return subr

for a in ['abcb','abcdaca', 'aabbccdc', 'abcdef', 'pqqrsstuvtt']:
    print(recSol(a))