#!/usr/bin/python3
#https://practice.geeksforgeeks.org/problems/a-simple-fraction/0

def sol(n, d):
    res = []
    r = {}

    i = int(n/d)
    rem = n%d
    res.append(i)

    if rem:
        res.append(".")
        r[rem] = 0
        p = 1

    while rem:
        div = rem*10
        q = div//d
        rem = div%d
        res.append(q)
        
        if rem in r:
            res.append(")")
            res.insert(r[rem]+2, "(")
            break
        else:
            r[rem] = p
            p+=1
    
    print("".join(str(x) for x in res))

sol(22, 7)
sol(23, 59)
sol(94, 36)
sol(4, 2)
sol(10, 4)
sol(70, 68)
