#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/replace-by-x/0

def sol(s, pat):
    """
    Take another string and keep copying the patterns
    If the pattern is found, keep looking for again and again in the continuity
    and finall copy an X in the result string
    """
    res = ""
    np = len(pat)
    
    i=0
    while i<len(s):
        if s[i:i+np] == pat:
            while s[i:i+np] == pat:
                i=i+np
            res+='X'
        else:
            res+=s[i]
            i+=1
    return res