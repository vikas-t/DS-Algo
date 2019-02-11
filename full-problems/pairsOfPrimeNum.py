#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/pairs-of-prime-number/0

def getPrimes(n):
    primes = [True]*(n+1)
    primes[0] = False
    primes[1] = False
    
    i=2
    while i*i<=n:
        if primes[i]:
            for j in range(2*i, n+1, i):
                primes[j] = False
        i+=1
    return primes

def sol(n):
    p = []
    i = 2
    while i <= n//2:
        if primes[i]:
            p.append(i)
        i+=1
    # Get all the prime numbers till n/2 because 2 is the smallest prime
    # number so the highest prime number that can be included cannot be 
    # more than n/2
    
    for i in range(len(p)):
        for j in range(len(p)):
            if p[i]*p[j] <= n:
                print(p[i], p[j], end=" ")
    print()