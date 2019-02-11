#!/usr/bin/python3
#https://practice.geeksforgeeks.org/problems/level-order-traversal/1 

def traverse_level_order(root, level=0, h={}):
    """
    Use a dictionary where height is the key and the nodes at the same height
    are the values. Collect all the nodes in the same fashion.
    At the end of level 0, print the values
    """
    if root:
        if level in h:
            h[level].append(root.data)
        else:
            h[level] = [root.data]
        traverse_level_order(root.left, level+1, h)
        traverse_level_order(root.right, level+1, h)
    
    if level == 0:
        for l in h:
            for data in h[l]:
                print(data, end=" ")