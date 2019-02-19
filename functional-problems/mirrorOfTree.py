#!/usr/bin/python
# Convert a tree in to its mirror tree i.e left and right subtrees are swapped

def mirrorTree(root):
    if root == None:
        return
    
    mirrorTree(root.left)
    mirrorTree(root.right)

    tmp = root.left
    root.left = root.right
    root.right = tmp