#!/usr/bin/python
#https://practice.geeksforgeeks.org/problems/permutations-of-a-given-string/0

res = []
def permute(a, l, r):
    if l==r:
        res.append("".join(a))
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]

for _ in range(int(input())):
    s = input()
    res=[]
    permute(list(s), 0, len(s)-1)
    for x in sorted(res):
        print(x, end=" ")
    print()