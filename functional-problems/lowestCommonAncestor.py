#!/usr/bin/python
# https://practice.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-bst/1

def LCA(root, a, b):
    """
    We can use the BST property that the smaller nodes lie on the left side
    and the larger on the right side of the root
    """
    if not root:
        return False
    if a > root.data and b > root.data:
        return LCA(root.right, a, b)
    elif a < root.data and b < root.data:
        return LCA(root.left, a, b)
    
    return root