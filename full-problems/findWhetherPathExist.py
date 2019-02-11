#!/usr/bin/python
# https://practice.geeksforgeeks.org/problems/find-whether-path-exist/0

moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#!careful about the moves

def isValid(mat, n, x, y):
    if x >= n or y >= n:
        return False
    if mat[x][y] == 0:
        return False
    return True
    
def sol(mat, n, sx, sy, dx, dy):
    """
    BFS solution just like knight walk
    """
    v = [[False for _ in range(n)] for _ in range(n)]
    v[sx][sy] = True
    
    q = []
    q.append((sx, sy))
    
    while q:
        sx, sy = q[0]
        q.pop(0)
        
        if sx == dx and sy == dy:
            return True
        
        for move in moves:
            nx, ny = sx + move[0], sy + move[1]
            
            if isValid(mat, n, nx, ny) and not v[nx][ny]:
                v[nx][ny] = True
                q.append((nx, ny))
    return False