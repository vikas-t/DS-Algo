#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/max-level-sum-in-binary-tree/1

def maxLevelSum(root):
    # Code here
    h = {}
    level = 0
    getLevelSum(root, level, h)
    return max(h.values())
    
def getLevelSum(root, level, h):
    if root == None:
        return
    
    if level not in h:
        h[level] = 0
    
    h[level] += root.data
    getLevelSum(root.left, level+1, h)
    getLevelSum(root.right, level+1, h)