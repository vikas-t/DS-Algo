#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/x-total-shapes/0

## Standard DFS application

moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
# The allowed moves in the question are only up down left and right

def isValid(arr, m, n, x, y, v):
    if x < 0 or x >=m or y < 0 or y >= n:
        return False
    if arr[x][y] == 'X' and not v[x][y]:
        return True
    return False

def formShape(arr, m, n, i, j, v):
    """
    Use recursion to trace the shape. We need not return just mark the cells
    visited
    """
    v[i][j] = True
    
    for move in moves:
        x, y = i+move[0], j+move[1]
        if isValid(arr, m, n, x, y, v):
            formShape(arr, m, n, x, y, v)

def sol(arr, m, n):
    """
    Visit every cell that is not visited, trace the shape and for every
    new shape increment the result
    """
    v = [[False for _ in range(n)] for _ in range(m)]
    c = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 'X' and not v[i][j]:
                formShape(arr, m, n, i, j, v)
                c+=1
    return c