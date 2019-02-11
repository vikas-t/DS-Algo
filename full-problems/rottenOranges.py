#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/rotten-oranges/0

def isRotten(mat, r, c, x, y):
    if 0 <= x < r and 0 <= y < c:
        if mat[x][y] == 1:
            return True
    return False

def sol(mat, r, c):
    """
    A straight forward BFS approach
    """
    q = []
    for i in range(r):
        for j in range(c):
            if mat[i][j] == 2:
                q.append((i, j, 0))
    # Lets collect all rotten oranges in a queue
    
    t = 0
    while q:
        # We keep marking all the fresh oranges rotten which are adjacent
        # to the rotten ones. We keep increasing the value of time by 1
        x, y, t = q.pop(0)
        for adj in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            nx, ny = x+adj[0], y+adj[1]
            if isRotten(mat, r, c, nx, ny):
                mat[nx][ny] = 2
                q.append((nx, ny, t+1))
    
    for i in range(r):
        if 1 in mat[i]:
            # If fresh oranges are left, we return -1
            return -1
    
    return t