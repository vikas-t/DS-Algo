#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/number-of-groups/0

# Check possibleGroups.py for explanation

def sol(arr, n):
    rem = {0: 0, 1: 0, 2: 0}
    
    for x in arr:
        rem[x%3]+=1
    
    res = 0
    res += (rem[0]*(rem[0]-1))//2
    res += rem[2]*rem[1]
    res += rem[2]*rem[1]*rem[0]
    res += (rem[0]*(rem[0]-1)*(rem[0]-2))//6
    res += (rem[1]*(rem[1]-1)*(rem[1]-2))//6
    res += (rem[2]*(rem[2]-1)*(rem[2]-2))//6
    
    return res