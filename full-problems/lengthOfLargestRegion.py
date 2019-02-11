#!/usr/bin/python3
#https://practice.geeksforgeeks.org/problems/length-of-largest-region-of-1s/0

def isRegion(mat, x, y, m, n, v):
    if 0 <= x < m and 0 <= y < n:
        if mat[x][y] == 1 and v[x][y] == False:
            return True
    return False

def findRegion(mat, x, y, m, n, v):
    """
    BFS to find the region and keep counting the area for every valid cell
    """
    q = []
    area = 1
    q.append((x, y))
    v[x][y] = True
    
    while q:
        x, y = q.pop(0)
        for move in moves:
            nm, ny = x+move[0], y+move[1]
            if isRegion(mat, nm, ny, m, n, v):
                q.append((nm, ny))
                v[nm][ny] = True
                area+=1
    return area

def sol(mat, m, n):
    """
    Visit every cell and if it is 1 and not visited already trace the region
    We use BFS here, check xTotalShapes where a similar question is done
    using DFS i.e recursion
    """
    v = [[False for _ in range(n)] for _ in range(m)]
    
    res = 0
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1 and not v[i][j]:
                res = max(res, findRegion(mat, i, j, m, n, v))
    return res      

moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
for _ in range(int(input())):
    m, n = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    mat = [[0 for _ in range(n)]for _ in range(m)]
    k = 0
    for i in range(m):
        for j in range(n):
            mat[i][j] = arr[k]
            k+=1
    print(sol(mat, m, n))