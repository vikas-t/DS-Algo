#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/tic-tac-toe/0

def sol(arr):
    cx = 0
    co = 0
    
    for i in range(3):
        for j in range(3):
            if arr[i][j] == "X":
                cx+=1
            else:
                co+=1
    # Count the zeroes and ones
    
    if cx-co != 1:
        return False
    # The count should not differ by more than 1 but because X starts the game
    # X should always be higher
    winner = []
    
    ds1 = 0  
    # Sum of one diagonal
    ds2 = 0  
    # Sum of another diagonal
    for i in range(3):
        rs = 0 # row sum
        cs = 0 # col sum
        
        for j in range(3):
            rs += ord(arr[i][j])
            cs += ord(arr[j][i])
            if i == j:
                ds1 += ord(arr[i][j])
            if i+j == 2:
                ds2 += ord(arr[i][j])
        
        if rs == 88*3 or cs == 88*3 or ds1 == 88*3 or ds2 == 88*3:
            winner.append('X')
        # ASCII of 'O' is 79 and 'X' is 88
        if rs == 79*3 or cs == 79*3 or ds1 == 79*3 or ds2 == 79*3:
            winner.append('O')
        # Check all the winners
    
    if 'O' in winner and 'X' in winner:
        return False
    # There cannot be two winners
    # Careful about incorrect synatx ******* if 'O' and 'X' in winner **** 
    if 'O' in winner and cx == 5:
        return False
    # If O wins it X will not get to play his last turn because X started the
    # game
    return True