#!/usr/bin/python3
#https://practice.geeksforgeeks.org/problems/sum-of-two-numbers-represented-as-arrays/0

def sol(a, b, m, n):
    res = []
    la = m-1
    lb = n-1
    carry = 0
    while la >= 0 or lb >= 0:
        x = int(a[la]) if la >= 0 else 0
        y = int(b[lb]) if lb >= 0 else 0
        s = (x+y+carry)%10
        carry = (x+y+carry)//10
        res.append(s)
        la-=1
        lb-=1
    if carry:
        res.append(carry)
    return " ".join(str(x) for x in reversed(res))