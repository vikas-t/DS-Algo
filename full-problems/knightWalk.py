#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/knight-walk/0

import sys

moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

def isValid(x, y, m, n):
    #print(x, y, m, n)
    if x < 1 or y < 1:
        return False
    if  x > m or y > n:
        return False
    return True

def sol(board, m, n, cx, cy, dx, dy):
    """
    It is not possible to do it this way as the visited cells are marked.
    So other ways cannot use the cell leading to incorrect cell
    """
    board[cx][cy] = True
    if cx == dx and cy == dy:
        print("ok")
        return 0
    
    moveCount = sys.maxsize
    for move in moves:
        nx, ny = cx+move[0], cy+move[1]
        if isValid(board, nx, ny, m, n):
            print(nx, ny)
            moveCount = min(moveCount, 1 + sol(board, m, n, nx, ny, dx, dy))
    
    return moveCount

def solBFS(m, n, cx, cy, dx, dy):
    """
    Unlike recursion this marks the steps going Breadth wise first. So at 
    every step all the next step(one away) are marked visited.
    The first one to reach the destination will be the minimum
    """
    q = []
    q.append((cx, cy, 0))
    isVisited = [[False for _ in range(n+1)]for _ in range(m+1)]
    isVisited[cx][cy] = True
    
    while q:
        t = q[0]
        print(t, q)
        q.pop(0)

        if t[0] == dx and t[1] == dy:
            return t[2]
        
        for move in moves:
            nx, ny = t[0]+move[0], t[1]+move[1]
            if isValid(nx, ny, m, n) and not isVisited[nx][ny]:
                q.append((nx, ny, t[2]+1))
                isVisited[nx][ny] = True

m, n = 4, 7
cx, cy, dx, dy = 2, 6, 2, 4
board = [[False for _ in range(n)] for _ in range(m)]
#print(sol(board, m, n, cx-1, cy-1, dx-1, dy-1))
print(solBFS(m, n, cx, cy, dx, dy))