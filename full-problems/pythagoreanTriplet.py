#!/usr/bin/python

# https://practice.geeksforgeeks.org/problems/pythagorean-triplet/0

def sol(arr):
    tmp = [i*i for i in arr]
    tmp.sort()
    n = len(tmp)

    #print(tmp)
    for i in range(n-1, 1, -1):
        a = tmp[i]
        l = 0
        r = i-1
        while l < r:
            if tmp[l] + tmp[r] == a:
                return True
            elif tmp[l] + tmp[r] > a:
                r = r-1
            else:
                l = l+1
    return False