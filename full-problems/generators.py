#!/usr/bin/python3
# Generators

def ex1():
    yield 0
    yield 1

    cnt = 2 
    a = 0
    b = 1
    c = a + b

    while cnt < 100:
        c = a + b
        yield c
        a = b
        b = c
        cnt += 1
    
print(ex1())