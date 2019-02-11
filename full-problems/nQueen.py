#!/usr/bin/python3
#https://practice.geeksforgeeks.org/problems/n-queen-problem/0

queens = []
results = []

def isValidNaive(grid, N, x, y):
    for i in range(N):
        if grid[x][i] == True:
            #print('x', i)
            return False
    
    for i in range(N):
        if grid[i][y] == True:
            #print(i, 'y')
            return False
    
    tx, ty = x+1, y+1
    while tx < N and ty < N:
        if grid[tx][ty] == True:
            #print(+1, tx, ty)
            return False
        tx+=1
        ty+=1

    tx, ty = x-1, y-1
    while tx >= 0 and ty >= 0:
        if grid[tx][ty] == True:
            #print(-1, tx, ty)
            return False
        tx-=1
        ty-=1
    
    tx, ty = x-1, y+1
    while tx >= 0 and ty < N:
        if grid[tx][ty] == True:
            return False
        tx-=1
        ty+=1

    tx, ty = x+1, y-1
    while tx < N and ty >= 0:
        if grid[tx][ty] == True:
            return False
        tx+=1
        ty-=1

    return True

def nQueenNaive(grid, N, n):
    #print(N, n, x, y)
    if n == 0:
        return True
    for i in range(N):
        for j in range(N):
            if not isValid(grid, N, i, j):
                continue
            grid[i][j] = True
            if nQueen(grid, N, n-1):
                return True
            grid[i][j] = False
    return False

def solNaive():
    # The naive way
    # Prints all possible solutions
    N=4
    res = []
    for i in range(N):
        for j in range(N):
            grid = [[False for _ in range(N)] for _ in range(N)]
            # The functions above modify the orginal grid, so we make a new 
            # one again and again
            grid[i][j] = True
            if nQueenNaive(grid, N, N-1):
                if grid not in res:
                    res.append(grid)
    for r in res:
        print(r)
##************************************************************************

def isValid(grid, N, row, col):
    for i in range(N):
        # No horizontal attacks
        if grid[row][i]:
            return False
    
    # We do not check the right side here as it is not yet filled
    r, c = row-1, col-1
    while r >= 0 and c >= 0:
        # No left up diagonal attacks
        if grid[r][c]:
            return False
        r-=1
        c-=1
    
    r, c = row+1, col-1
    while r < N and c >= 0:
        # No left down diagonal attacks
        if grid[r][c]:
            return False
        r+=1
        c-=1
    
    return True

def nQueen(grid, N, n, col):
    if n >= N:
        results.append(queens[:])
        return
    
    for i in range(N):
        if isValid(grid, N, i, col):
            queens.append(i+1)
            grid[i][col] = True
            nQueen(grid, N, n+1, col+1)
            # For every valid arrangement, recurse till N is exhausted and
            # keep appending the results
            # Note that its not returning at any points making sure that
            # every combination is tried at every level
            grid[i][col] = False
            queens.remove(i+1)
            # Undo the changes one sub results are appended

def sol():
    N=4
    grid = [[False for _ in range(N)] for _ in range(N)]
    nQueen(grid, N, 0, 0)
    if results:
        for r in results:
            print("["+" ".join(str(x) for x in r)+" ]", end=" ")
            # Print as per required in the question
    else:
        print(-1)
sol()