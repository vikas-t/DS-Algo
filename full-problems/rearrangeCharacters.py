#!/usr/bin/python3
#https://practice.geeksforgeeks.org/problems/rearrange-characters/0

def sol(s):
    """
    If a character frequency is 4 then it requires atleast 3 other 
    characters so that the characters are not adjacent. We only need to
    check the character with highest frequency because if those are not 
    adjacent then no other can be adjacent
    """
    n = len(s)
    arr=[0]*26
    for x in s:
        arr[ord(x)-97] +=1
    maxf = max(arr)
    if n == 1:
        return 1
    # For a single character
    
    if maxf >= n-maxf+1: 
        return 0
    
    return 1

print(sol("geeksforgeeks"))
print(sol("bbbbb"))
print(sol("hhhhhjjjjjfff"))
