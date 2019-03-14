#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/two-mirror-trees/1

def mirrorTrees(a, b):
    if a == None and b == None:
        return True
    elif a == None:
        return False
    elif b == None:
        return False
    
    return a.data == b.data \
           and mirrorTrees(a.left, b.right)
           and mirrorTrees(a.right, b.left)