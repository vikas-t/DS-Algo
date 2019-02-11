#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/diameter-of-binary-tree/1

def diameter(root):
    d,_ = getDiameter(root)
    return d
    
def getDiameter(root):
    if root == None:
        return 0, 0
    
    ld, lh = getDiameter(root.left)
    rd, rh = getDiameter(root.right)
    
    return max(ld, rd, lh+rh+1), 1+max(lh, rh)
