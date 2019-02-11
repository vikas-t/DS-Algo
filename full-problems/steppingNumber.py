#!/usr/bin/python3
#https://practice.geeksforgeeks.org/problems/stepping-numberswrong-output/0


def bfs(x, n, res):
    """
    The stepping number is generated from existing stepping numbers
    for ex: 1 generates 12, 10
            2  generates 21, 23
    """
    q = []
    q.append(x)

    while q:
        p = q.pop(0)

        if p <= n:
            res.append(p)
            d = p%10
            if d == 0:
                q.append(p*10+(d+1))
            elif d == 9:
                q.append(p*10+(d-1))
            else:
                q.append(p*10+(d+1))
                q.append(p*10+(d-1))
    return res

def sol(m, n):
    res = []
    for i in range(1, 10):
        # Start finding the number breadth wise order using the initial numbers
        bfs(i, n, res)
    
    c = 0
    for r in res:
        if r >=m:
            c+=1
    
    if m == 0:
        return c+1
    return c 

print(sol(0, 21))