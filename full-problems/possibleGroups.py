#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/possible-groups/0

def sol(arr):
    """
    The sum of numbers are divisible by 3 if the sum of their remainders are
    divisible by 3.
    For example : 8, 4, 12. Now, the remainders are 2, 1, and 0 respectively.
    This means 8 is 2 distance away from 3s multiple (6), 4 is 1 distance 
    away from 3s multiple(3), and 12 is 0 distance away. 
    So, we can write the sum as 8 (can be written as 6+2), 
    4 (can be written as 3+1), and 12 (can be written as 12+0). 
    Now the sum of 8, 4 and 12 can be written as 6+2+3+1+12+0. 
    Now, 6+3+12 will always be divisible by 3 as all the terms are multiple 
    of three. 
    Now, we only need to check if 2+1+0 (remainders) is divisible by 3 or 
    not which makes the complete sum divisible by 3.
    """
    rem = {2: 0, 1: 0, 0: 0}
    for x in arr:
        r = x%3
        rem[r] = rem[r] + 1 
    
    res = 0
    # The 0, 0 case
    res += (rem[0]*(rem[0]-1))//2
    # The sum can be 0 and for a group of two remainders can be 0 and 0
    
    # The 2, 1 case
    res += rem[2]*rem[1]
    # The sum can be 3 and remainders can be 2 and 1 in a group of two
    
    # The 0, 0, 0 case
    res += (rem[0]*(rem[0]-1)*(rem[0]-2))//6
    # Remainders 0, 0 and 0 for a group of three and follow the rest

    # The 2, 1, 0 case
    res += rem[2]*rem[1]*rem[0]

    # The 1, 1, 1 case
    res += (rem[1]*(rem[1]-1)*(rem[1]-2))//6
    
    # The 2, 2, 2
    res += (rem[2]*(rem[2]-1)*(rem[2]-2))//6

    return res

print(sol([3, 6, 2, 7, 9]))