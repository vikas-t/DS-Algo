#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/count-subsequences-of-type-ai-bj-ck/0

def isSol(res):
    """
    Check if the string is of the type ai bj ck
    """
    if not res or res[0] != 'a' or res[-1] != 'c':
        return False

    l = 0
    r = len(res)-1

    while res[l] == "a":
            l+=1
    
    while res[r] == "c":
            r-=1
    
    if r-l+1 <= 0:
        return False
    
    for x in res[l:r-l+1]:
        if x != 'b':
            return False
    
    return True

def sol(s, n, res=""):
    """
    Recursive solution
    """
    if isSol(res):
        return 1
    if n <= 0:
        return 0
    return sol(s, n-1, s[n-1]+res) + sol(s, n-1, res)

#############################################################################
"""
We traverse given string. For every character encounter, we do following:

1) Initialize counts of different subsequences caused by different 
   combination of ‘a’. Let this count be aCount.

2) Initialize counts of different subsequences caused by different 
   combination of ‘b’. Let this count be bCount.

3) Initialize counts of different subsequences caused by different 
   combination of ‘c’. Let this count be cCount.

4) Traverse all characters of given string. Do following for current character s[i]
    If current character is ‘a’, then there are following possibilities :
    a) Current character begins a new subsequence.
    b) Current character is part of aCount subsequences.
    c) Current character is not part of aCount subsequences.
    Therefore we do aCount = (1 + 2 * aCount);

    If current character is ‘b’, then there are following possibilities :
    a) Current character begins a new subsequence of b’s with aCount subsequences.
    b) Current character is part of bCount subsequences.
    c) Current character is not part of bCount subsequences.
    Therefore we do bCount = (aCount + 2 * bCount);

    If current character is ‘c’, then there are following possibilities :
    a) Current character begins a new subsequence of c’s with bCount subsequences.
    b) Current character is part of cCount subsequences.
    c) Current character is not part of cCount subsequences.
    Therefore we do cCount = (bCount + 2 * cCount);

5) Finally we return cCount;
"""

def sol2(s):
    """
    Real solution
    """
    a = b = c = 0
    for x in s:
        if x == "a":
            a = 1 + 2*a
        elif x == "b":
            b = a + 2*b
        elif x == "c":
            c = b + 2*c
    return c

cases = ["abbc", "abcabc", "abc"]
for case in cases:
    print(sol(case, len(case)))