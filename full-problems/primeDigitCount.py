#!/usr/bin/python

#https://practice.geeksforgeeks.org/problems/find-the-highest-occurring-digit-in-prime-numbers-in-a-range/0

def isPrime(n):
    if n < 2: return False
    sqrtn = int(n**0.5)
    for i in range(2, sqrtn+1):
        if n%i==0:
            return False
    return True

def sieveOfEratosthenes(n):
    listInt = [True for i in range(n+1)]
    listInt[0] = False
    listInt[1] = False
    p = 2

    while p*p<=n:
        if listInt[p]:
            for i in range(2*p, n+1, p):
                listInt[i] = False
        p+=1
    return listInt
    
def sol(l, r):
    primes = sieveOfEratosthenes(r+1)
    count = [0]*10
    for i in range(l, r+1):
        if not primes[i]:
            continue
        tn = i
        while tn:
            d = int(tn%10)
            count[d] += 1
            tn = tn/10
    
    mx = -1
    mxp = -1
    print(count)
    for i in range(1, 10):
        if count[i] >= mx:
            mx = count[i]
            mxp = i
    return mxp

print(sol(2, 1000000))
