#!/usr/bin/python3
# http://www.geeksforgeeks.org/category/program-output/

def isIdentical(root1, root2):
    if root1 == None and root2 == None:
        return True
    elif root1 and root2:
        return root1.data == root2.data and isIdentical(root1.left, root2.left) and isIdentical(root1.right, root2.right)
    return False
