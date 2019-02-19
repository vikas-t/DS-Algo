#!/usr/bin/python3

# https://practice.geeksforgeeks.org/problems/delete-a-node-from-bst/1


def minValueNode(root):
    """
    Returns the iorder successor or the next higher node as per 
    the inorder traversal
    """
    current = root
  
    # loop down to find the leftmost leaf 
    while(current.left is not None): 
        current = current.left  
  
    return current

def deleteNode(root, key):
    if root == None:
        return 
    
    if key < root.data:
        root.left = deleteNode(root.left, key)
    # If the key to be deleted is smaller than the root's 
    # key then it lies in  left subtree 
    
    elif key > root.data:
        root.right = deleteNode(root.right, key)
    # If the key to be deleted is greater than the root's 
    # key then it lies in right part
    
    else:
    # The key is same as root's key, then this is the node to be deleted 
        if root.left == None:
            tmp = root.right
            root = None
            return tmp
        elif root.right == None:
            tmp = root.left
            root = None
            return tmp
        # Convers cases when there is only one child of the root or no child
        
        v = minVal(root.right)
        # When both nodes exists, get the inorder successor 
        root.data = v.data
        root.right = deleteNode(root.right, v.data)
        # Delete the inorder successor

        return root

        
