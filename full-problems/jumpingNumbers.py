#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/jumping-numbers/0

from functools import cmp_to_key

def comp(a, b):
    x = str(a)
    y = str(b)
    if int(x[0]) < int(y[0]):
        return -1
    elif int(x[0]) > int(y[0]):
        return 1
    else:
        if a > b:
            return 1
        return -1

def isJumpingNo(n):
    x = list(str(n))
    if len(x) == 1:
        return True
    for i in range(len(x)-1):
        if (x[i] == '0' and x[i+1] == '9') or (x[i] == '9' and x[i+1] == 0):
            return False
        if abs(int(x[i]) - int(x[i+1])) != 1:
            return False
    return True

def sol():
    res = []
    for i in range(100002):
        if isJumpingNo(i):
            res.append(i)
    return res

res = sol()
l = len(res)
for _ in range(int(input())):
    n = int(input())
    i = 0
    t = []
    while i<l and res[i] <= n:
        t.append(res[i])
        i+=1
    for e in sorted(t, key=cmp_to_key(comp)):
        print(e, end=" ")
    print()

# Best sol using BFS***********************************************
# Prints all jumping numbers smaller than or equal to
# x starting with 'num'. It mainly does BFS starting
# from 'num'.
def bfs(x,num):
 
    # Create a queue and enqueue i to it
    q = Queue()
    q.enqueue(num)
 
    # Do BFS starting from 1
    while (not q.is_empty()):
        num = q.dequeue()
 
        if num<=x:
            print(str(num),end=' ')
            last_dig = num % 10
 
            # If last digit is 0, append next digit only
            if last_dig == 0:
                q.enqueue((num * 10) + (last_dig + 1))
 
            # If last digit is 9, append previous digit
            # only
            elif last_dig == 9:
                q.enqueue((num * 10) + (last_dig - 1))
 
            # If last digit is neighter 0 nor 9, append
            # both previous digit and next digit
            else:
                q.enqueue((num * 10) + (last_dig - 1))
                q.enqueue((num * 10) + (last_dig + 1))
 
# Prints all jumping numbers smaller than or equal to
# a positive number x
def printJumping(x):
    print (str(0), end=' ')
    for i in range(1, 10):
        bfs(x, i)