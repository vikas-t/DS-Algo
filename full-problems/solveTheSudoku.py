#!/usr/bin/python
#https://practice.geeksforgeeks.org/problems/solve-the-sudoku/0

def findEmptyCell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None

def isValid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num:
            return False
    
    for i in range(9):
        if board[i][col] == num:
            return False

    row = row-row%3
    col = col-col%3
    for i in range(3):
        for j in range(3):
            if board[i+row][j+col] == num:
                return False
    return True

def sol(board):
    """
    Plain backtracking, find which cell is empty and assign the number. 
    Return on first True
    """
    row, col = None, None
    row, col = findEmptyCell(board)
    
    if row  == None and col == None:
        # Careful about using 'not row'
        return True

    for num in range(1, 10):
        if isValid(board, row, col, num):
            board[row][col] = num
            if sol(board):
                return True
            board[row][col] = 0
    return False
    
arr = "0 0 0 0 0 0 0 6 0 4 7 1 0 2 0 0 0 0 9 6 0 0 8 1 0 0 0 8 0 0 2 0 0 0 7 0 0 5 0 8 0 7 0 9 0 0 9 0 0 0 3 0 0 1 0 0 0 3 7 0 0 1 5 0 0 0 0 9 0 4 3 2 0 3 0 0 0 0 0 0 0"

arr = list(map(int, arr.split()))
board = [[0 for _ in range(9)] for _ in range(9)]
k = 0
for i in range(9):
    for j in range(9):
        board[i][j] = arr[k]
        k+=1
sol(board)
print(board)