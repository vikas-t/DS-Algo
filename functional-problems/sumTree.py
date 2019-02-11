#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/sum-tree/1

def isSumTree(root):
    """
    If the tree is a sumTree then 2*ls = root.data or 2*rs = root.data
    If its a Leaf its a sumTree 
    If its None its a sumTree
    """
    ls = rs = 0
    
    if not root or isLeaf(root):
        return True
    
    if isSumTree(root.left) and isSumTree(root.right):
        if not root.left:
            ls = 0
        elif isLeaf(root.left):
            ls = root.left.data
        else:
            ls = 2*(root.left.data)
        
        if not root.right:
            rs = 0
        elif isLeaf(root.right):
            rs = root.right.data
        else:
            rs = 2*(root.right.data)
        
        return ls + rs == root.data
        
        
def isLeaf(root):
    if not root:
        return False
    if not root.left and not root.right:
        return True