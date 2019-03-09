#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/construct-tree-from-preorder-traversal/1

def constructTree(pre, preLn, n):
    idxCount = [0]
    # This to keep track(via reference) of the index in the 
    # pre order traveral list
    buildTree(pre, preLn, idx, n)

def buildTree(pre, preLn, idxCount, n):
    idx = idxCount[0]
    if idx >= n:
        return None
    # Once 'n' reaches out of bound we return
    
    node = Node(pre[idx])
    idxCount[0] += 1

    if preLn[idx] == 'N':
        node.left = buildTree(pre, preLn, idxCount, n)
        node.right = buildTree(pre, preLn, idxCount, n)
    
    return node