#!/usr/bin/python3
# Generators

def genFibonacci():
    """
    Fibonacci generator
    """
    yield 0
    yield 1

    cnt = 2 
    a = 0
    b = 1
    c = a + b

    while cnt < 10:
        c = a + b
        yield c
        a = b
        b = c
        cnt += 1

def genPrimes():
    n = 1000
    primes = [True]*(n+1)
    primes[0] = False
    primes[1] = False
    
    i = 2
    while i*i <= n:
        if primes[i]:
            yield i
            for j in range(2*i, n+1, i):
                primes[j] = False
        i+=1
    
#for i in genFibonacci():
#    print(i)

cnt = 1
for p in genPrimes():
    if cnt==1:
        print(p)
        break
    cnt+=1