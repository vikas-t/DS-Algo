#!/usr/bin/python
# https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1

def printLeftView(root):
    # Get the level order traversal of the tree and print the first node
    # of each level
    levelOrder = getLevelOrder(root, h={})
    for level in levelOrder:
        print(levelOrder[level][0], end=" ")

def getLevelOrder(root, level=0, h={}):
    # Be careful when you use a default mutable argument in the function
    if root:
        if level in h:
            h[level].append(root.data)
        else:
            h[level] = [root.data]
        getLevelOrder(root.left, level+1, h)
        getLevelOrder(root.right, level+1, h)
    if level == 0:
        return h