#!/usr/bin/python
#https://practice.geeksforgeeks.org/problems/longest-prefix-suffix/0

def sol(s):
    """
    Starting from 0 check which positions have the same letter as the last 
    one and store them in a list.
    Next, starting from the last in the list check the string to the left.
    """
    n = len(s)
    mbs = []
    for i in range(n-1):
        if s[i] == s[n-1]:
            mbs.append(i)
    
    c=0
    for st in mbs[::-1]:
        c = 0
        l = st
        r = n-1
        while l >= 0:
            if s[l] == s[r]:
                c+=1
            else:
                break
            l-=1
            r-=1
        if l < 0:
            return c
    return c

def computeLPS(s, n):
    """
    Sol with better comle
    """
    prev = 0 # length of the previous longest prefix suffix
    lps = [0]*(n)
    i = 1
 
    # the loop calculates lps[i] for i = 1 to n-1
    while i < n:
        if s[i] == s[prev]:
            prev += 1
            lps[i] = prev
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar 
            # to search step.
            if prev != 0:
                prev = lps[prev-1]
 
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1
    print(lps)
    return lps[n-1]

s = "abcdeabcab"
print(sol(s))
print(computeLPS(s, len(s)))