#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/find-k-th-character-in-string/0
def toBinary(n):
    res = ''
    while n > 0:
        res = str(n%2) + res
        n = n//2
    return res

def sol(m , k, n):
    arr = list(toBinary(m))
    while n:
        ts = []
        #print(arr)
        for x in arr:
            if x == '1':
                ts.append('10')
            else:
                ts.append('01')
        arr = list(''.join(x for x in ts))
        n-=1
    r = ''.join(x for x in ts)
    return r[k]