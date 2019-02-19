#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/diameter-of-binary-tree/1

def diameter(root):
    d,_ = getDiameter(root)
    return d
    
def getDiameter(root):
    if root == None:
        return 0, 0
    
    ld, lh = getDiameter(root.left)
    # Get left diameter and height of left subtree
    rd, rh = getDiameter(root.right)
    # Get right diamtere and heigght of right subtree    
    
    return max(ld, rd, lh+rh+1), 1+max(lh, rh)
    # So diameter of a tree is the maximum of diamters of left subtree and 
    # diameter of the right subtree and the longest path that goes through
    # the root (basically height of left subtree + height of right subtree + 1)
 