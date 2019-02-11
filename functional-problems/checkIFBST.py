#!/usr/bin/python3

def isBST(node, mn=-1*sys.maxsize, mx=sys.maxsize):
    if not node:
        return True
    # Empty is BST

    if node.data < mn or node.data > mx:
        return False
    
    return isBST(node.left, mn, node.data-1) and isBST(node.right, node.data+1, mx)
    # The left side of the tree can go to any minimum but its max should be 
    # less than its parent
    # Likewise, the right side of the tree can go to any maximim but its min 
    # value should be bound by the max value of its parent
