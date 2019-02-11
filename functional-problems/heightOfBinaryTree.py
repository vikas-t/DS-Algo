#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/height-of-binary-tree/1

def getHeight(root):
    """
    Start with 0 height and recurse going down, increasing the levels
    """
    if not root:
        return 0
    return 1 + max(getHeight(root.left), getHeight(root.right))