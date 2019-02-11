#!/usr/bin/python3
#https://practice.geeksforgeeks.org/problems/string-formation-from-substring/0

def sol(s):
    """
    It is quite clear that the substring will start from the first index
    itself otherwise, it cannot form the string
    Find all the indexes where the character is same as the first char, this
    implies the string may repeat from there. For all such indexes check 
    if any repeating t times can form the original string
    Other solution is to find out the longest prefix using the LPS method
    and check for repetition
    """
    n = len(s)
    i = 1
    if n == 1:
        return False
    
    aux = []
    while i < n//2+1:
        if s[i] == s[0]:
            aux.append(i)
        i+=1
    
    for x in aux:
        t = n//x
        if s[:x]*t == s:
            return True
    
    return False