#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/maximum-path-sum/1


"""
For each node there can be four ways that the max path goes through the node:
1. Node only
2. Max path through Left Child + Node
3. Max path through Right Child + Node
4. Max path through Left Child + Node + Max path through Right Child

The idea is to keep trace of four paths and pick up the max one in the end. 
An important thing to note is, root of every subtree need to return maximum 
path sum such that at most one child of root is involved. This is needed 
for parent function call. In below code, this sum is stored in ‘maxPart’ 
and returned by the recursive function.
"""

def findMaxPath(root):
    if root == None:
        return
    
    l = findMaxPath(root.left)
    r = findMaxPath(root.right)

    maxPart = max(max(l, r)+root.data, root.data)
    # At most one child is involved, so that this can be added to its parent
    # to extend the path. We return the same at the end of the recursion

    maxLocal = max(maxPart, l+r+root.data)
    # Consider that left+right+root can also be a path

    findMaxPath.res = max(maxLocal, findMaxPath.res)
    # Update the global encountered so far in a static variable

    return maxPart

def maxPathSum(root):
    findMaxPath.res = -1*sys.maxsize
    findMaxPath(root)
    return findMaxPath.res