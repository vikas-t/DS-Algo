#!/usr/bin/python
#  https://practice.geeksforgeeks.org/problems/relative-sorting/0

def sol(a, b, m, n):
    """
    Store the counts of each element, traverse through the second array and 
    keep building a temp. array, finally insert the elements which are not in
    the second array
    complextiy = m+n
    """
    me = max(a)
    c = [0 for i in range(me+1)]
    
    for x in a:
        c[x] += 1
        
    tmp = []
    
    for x in b:
        while c[x]:
            tmp.append(x)
            c[x] -= 1
    
    for i in range(me+1):
        while c[i]:
            tmp.append(i)
            c[i] -= 1
    
    for x in tmp:
        print(x, end=" ")
    print()