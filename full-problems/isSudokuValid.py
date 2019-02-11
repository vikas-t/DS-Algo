#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/is-sudoku-valid/0

def getEmptyCell(mat):
    for i in range(9):
        for j in range(9):
            if mat[i][j] == 0:
                return i, j
    return None, None
            
def isValid(x, y, num):
    for i in range(9):
        if mat[x][i] == num:
            return False
    
    for i in range(9):
        if mat[i][y] == num:
            return False
    
    r = (x//3)*3
    c = (y//3)*3
    for i in range(3):
        for j in range(3):
            if mat[r+i][c+j] == num:
                return False
    return True

def sol(mat):
    """
    If there exists a solution return 1, 0 otherwise
    """
    x, y = getEmptyCell(mat)
    
    if x == None and y == None:
        return 1
        
    for num in range(1, 10):
        if isValid(x, y, num):
            mat[x][y] = num
            if sol(mat):
                return 1
            mat[x][y] = 0
    return 0