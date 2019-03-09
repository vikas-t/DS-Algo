#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/odd-even-level-difference/1

def getLevelDiff(root):
    h = {0: 0, 1: 0}
    level = 0
    populateDiff(root, level, h)
    return h[0]-h[1]
    
def populateDiff(root, level, h):
    if root == None:
        return
    
    l = level%2
    h[l] += root.data
    
    populateDiff(root.left, level+1, h)
    populateDiff(root.right, level+1, h)