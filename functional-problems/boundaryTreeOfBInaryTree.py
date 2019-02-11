#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1

# One easy method is to do a level order traversal and print the first of every
# level in bottom down manner, then print the last element of every level in
# top up manner

def printBoundaryView(root):
    if root:
        print(root.data, end=" ")
    
        printLeft(root.left)
        printLeaves(root.left)
        printLeaves(root.right)
        printRight(root.right)

def printLeft(root):
    """
    Print the left in top down but not the leaves
    """
    if root:
        if root.left:
            print(root.data, end=" ")
            printLeft(root.left)
        elif root.right:
            print(root.data, end=" ")
            printLeft(root.right)
    
def printRight(root):
    """
    Print the right in bottom up but not the leaves
    """
    if root:
        if root.right:
            printRight(root.right)
            print(root.data, end=" ")
        elif root.left:
            printRight(root.left)
            print(root.data, end=" ")
            
def printLeaves(root):
    """
    Print all the nodes that have no children
    """
    if root:
        printLeaves(root.left)
        if not root.left and not root.right:
            print(root.data,end=" ")
        printLeaves(root.right)