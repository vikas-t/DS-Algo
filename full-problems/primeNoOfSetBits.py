#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/prime-number-of-set-bits/0

primes = []

def getPrimes(n):
    # Sieve of Eratosthenes
    primes = [True for i in range(n+1)]
    primes[0] = False
    primes[1] = False
    p = 2

    while p*p<=n:
        if primes[p]:
            for i in range(2*p, n+1, p):
                primes[i] = False
        p+=1
    return primes
    
def sol(l, r):
    res = 0
    for i in range(l, r+1):
        cnt = len([1 for x in bin(i)[2:] if x == '1'])
        # Convert to binary using bin and count the ones
        if primes[cnt]:
            res+=1
    return res
    
primes = getPrimes(1000001)
# Get all the prime numbers till the given range