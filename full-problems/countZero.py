#!/usr/bin/pythonn3
# https://practice.geeksforgeeks.org/problems/count-zero/0

def compute():
    # Precompute the values till given n
    res = [0]*(16)
    res[2] = 9
    
    for d in range(3, 16):
        res[d] = 9*(10**(d-1)) - 9**d
    # For a 4 digit no. Total numbers possible are 9*10*10*10
    # As the first place cannot take 0, rest all the places can take all the 
    # digits. So 9*(10**(d-1))
    # The numbers with non zeros are 9*9*9*9, so 9**d
    return res

def sol(n):
    r = 0
    for i in range(2, n+1):
        r+=res[i]
    # The questions states atleast one zero with d or less digits
    return r
    
res = compute()
for _ in range(int(input())):
    n = int(input())
    print(sol(n))