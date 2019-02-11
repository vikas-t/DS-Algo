#!/usr/bin/python3
#https://practice.geeksforgeeks.org/problems/permutation-with-spaces/0

def sol(s, n, space, res, st=0):
    """
    Recursive solution
    """
    if space == 0:
        res.append(s)
        return
    
    for i in range(st, n-space):
        sol(s[:i+1]+" "+s[i+1:], n+1, space-1, res, st=i+2)
        # We add a new " ", length of string increases by 1, so we new start
        # becomes i+2 instead of i+1

# Driver code        
for _ in range(int(input())):
    s = input()
    n = len(s)
    spaces=n-1
    res = []
    for space in range(spaces, -1, -1):
        # For all possible spaces, place the spaces
        sol(s, n, space, res)
    
    for x in sorted(res):
        # The problem wants the soln in sorted order, see how sorting works 
        # with spaces
        print("("+x+")", end="")
    print()