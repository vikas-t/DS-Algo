#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/check-if-given-four-points-form-a-square/0

def sqDist(x1, y1, x2, y2):
    """
    Returns the square of distance between two points
    """
    return (x1-x2)**2 + (y2-y1)**2

def sol(x1, y1, x2, y2, x3, y3, x4, y4):
    """
    Pick a point and calculate its distance with the rest of the points
    If any two are same and the third one is sqrt(2) times the distance
    obtained and the third one is also the same distance away from the 
    other two then its a Square
    """
    d2 = sqDist(x1, y1, x2, y2)
    d3 = sqDist(x1, y1, x3, y3)
    d4 = sqDist(x1, y1, x4, y4)
    
    if d2 == d3 and d4 == 2*d2 and d2 > 0:
        return sqDist(x4, y4, x2, y2) == d2 and sqDist(x4, y4, x3, y3) == d2
    
    if d2 == d4 and d3 == 2*d2 and d2 > 0:
        return sqDist(x3, y3, x2, y2) == d2 and sqDist(x3, y3, x4, y4) == d2
    
    if d3 == d4 and d2 == 2*d3 and d3 > 0:
        return sqDist(x2, y2, x3, y3) == d3 and sqDist(x2, y2, x4, y4) == d3
    
    return False