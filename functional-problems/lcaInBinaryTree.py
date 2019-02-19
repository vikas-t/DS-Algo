#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-binary-tree/1

# https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/
# Read explanation here

def findLCA(root, n1, n2):
    v = [False, False]
    
    lca = getLCA(root, n1, n2, v)
    if v[0] and v[1] or (v[0] and nodeInTree(root, n2)) or (v[1] and nodeInTree(root, n1)):
        return lca
    # The question arises where does v[0] is True but v[1] is False or
    # vice versa. Lets assume the n1 is a child of n2, then when the statement 
    # root.data == a becomes true, v[0] is set to True and it returns from
    # there, so v[1] is still set to false.    
    return None
    
def nodeInTree(root, k):
    """
    Checks if the node exists in the tree or not
    """
    if root == None:
        return False
    
    if root.data == k or nodeInTree(root.left, k) or nodeInTree(root.right, k):
        return True
    
    return False

def getLCA(root, a, b, v):
    """
    The method assumes that keys are present in Binary Tree. 
    If one key is present and other is absent, then it returns the present 
    key as LCA (Ideally should have returned NULL). To overcome this 
    we use findLCA() which is a wrapper over this
    """
    if root == None:
        return None
    
    if root.data == a:
        v[0] = True
        return root
    
    if root.data == b:
        v[1] = True
        return root
    
    llca = getLCA(root.left, a, b, v)
    rlca = getLCA(root.right, a, b, v)
    
    if llca and rlca:
        return root
    
    if not llca:
        return rlca
    
    if not rlca:
        return llca