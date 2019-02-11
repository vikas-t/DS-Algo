#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/level-order-traversal-in-spiral-form/1

# Again the simplest solution is to do a level order traversal and for every
# height keep changing the direction of printing the list

def printSpiralLevelOrder(root):
    """
    Fetch the height and for every height print the left and right leaf nodes
    This is also the way to do the level order traversal without aux space
    Worst case complexity of this recursive approach: 
    Worst case time complexity of the above method is O(n^2). Worst case occurs in case of skewed trees.
    """
    reverse = True
    height = getHeight(root)
    
    for h in range(1, height+1):
        printLevel(root, h, reverse)
        reverse = not(reverse)

def printLevel(root, level, reverse):
    if root==None:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        if reverse:
            printLevel(root.right, level-1, reverse)
            printLevel(root.left, level-1, reverse)
        else:
            printLevel(root.left,level-1, reverse)
            printLevel(root.right, level-1, reverse)

def getHeight(root):
    if not root:
        return 0
    return 1 + max(getHeight(root.left), getHeight(root.right))