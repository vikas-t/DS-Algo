#!/usr/bin/python3

"""
# Inorder Successor in Binary Search Tree
In Binary Tree, Inorder successor of a node is the next node in Inorder 
traversal of the Binary Tree. Inorder Successor is NULL for the last 
node in Inoorder traversal.
In Binary Search Tree, Inorder Successor of an input node can also be 
defined as the node with the smallest key greater than the key of input node. 
So, it is sometimes important to find next node in sorted order.
"""

def inorderSuccessor(root, n):
    # n is the key for which the successor has to be calculated
    if n.right != None:
        return minVal(root.right)

    succ = None
    while root:
        if n.data < root.data:
            succ = root
            root = root.left
        else:
            root = root.right

    return succ

def minVal(root):
    cur  = root
    while cur.left is not None:
        cur = cur.left
    return cur