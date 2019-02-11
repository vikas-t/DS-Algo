#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/does-robot-moves-circular/0

def sol(moves):
    x = y = 0
    d = 1
    dm = ["n", "e", "s", "w"]
    # Notice that it indexed clock wise
    
    for move in moves:
        if move == "G":
            if dm[d] == "e":
                y += 1
            elif dm[d] == "w":
                y -= 1
            elif dm[d] == "n":
                x += 1
            else:
                x -= 1
        elif move == "L":
            d = (4+d-1)%4
        # Left of North is w, left of West is South
        # Basically 1 index left in clock wise direction 
        else:
            d = (d+1)%4
        # 1 index to the right in clock wise

            
    return not x and not y

print(sol("GLGLGLG"))
print(sol("GLLG"))