import sys

def dfs(pos, snakes, ladders, lookup):
    """
    Solution using DFS, memoized lookup
    """
    if pos < lastPos and lookup[pos] != maxMoves:
        return lookup[pos]
    if pos > lastPos:
        return maxMoves

    for move in range(1, 7):
        #print(pos, move, lookup, snakes)
        nextPos = pos+move
        if nextPos in snakes:
            continue
        if nextPos in ladders:
            nextPos = ladders[nextPos]
        lookup[pos] = min(
            lookup[pos], 1+dfs(nextPos, snakes, ladders, lookup))
    return lookup[pos]

# **************Another solution******************

def isValid(pos, snakes):
    if pos <= lastPos and pos not in snakes:
        return True
    return False 

def bfs(pos, snakes, ladders):
    """
    Breadth first solution
    """
    q = []
    # We need not track the visited cells here
    
    q.append((pos, 0)) 
    # We store the current position as well as no. of 
    # moves required to reach here
    v[pos] = True

    while q:
        pos, moves = q.pop(0)
        if pos == lastPos:
            return moves
        
        for move in range(1, 7):
            nextPos = pos+move
            if nextPos in ladders:
                nextPos = ladders[nextPos]
            if isValid(nextPos, snakes):
                # The position is invalid if a snake is present
                q.append((nextPos, moves+1))

lastPos = 30
maxMoves = 30
# The row and column are fixed as 5 and 6
lookup = [maxMoves]*(lastPos+1)
lookup[lastPos] = 0
# The no. of moves required once we reach last position is 0
# We require the lookup while using recursive solution
snakes = {}; ladders={}
snakes[27] = 1
snakes[21] = 9
print(dfs(1, snakes, ladders, lookup))
print(bfs(1, snakes, ladders))