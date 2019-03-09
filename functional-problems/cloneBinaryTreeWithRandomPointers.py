#!/usr/bin/python
# https://practice.geeksforgeeks.org/problems/clone-a-binary-tree/1

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.random = None

def printTree(root):
    if root == None:
        return
    printTree(root.left)
    if not root.random:
        randData  = "None"
    else:
        randData = root.random.data
    print(root.data, "(", randData, ")", end="    ")
    printTree(root.right)

def cloneTreeUtil(root, root2, h):
    if root == None:
        return None
    
    root2 = Node(root.data)
    h[root] = root2 
    
    root2.left = cloneTreeUtil(root.left, root2.left, h)
    root2.right = cloneTreeUtil(root.right, root2.right, h)

    return root2

def cloneTree(root):
    h = {}
    root2 = None
    root2 = cloneTreeUtil(root, root2, h)
    
    for node in h:
        if node.random:
            h[node].random = h[node.random]
        else:
            h[node].random = None
    return root2

## driver code
n1 = Node(4)
n2 = Node(5)
n3 = Node(6)
n4 = Node(0)
n5 = Node(1)
n6 = Node(3)
n7 = Node(2)

n1.left = n2
n1.right = n3
n1.random = n5

n2.left = n4
n2.right = n5
n2.random = n7

n3.left = n6
n3.right = n7
n3.random = n1

printTree(n1)
print()
cn1 = cloneTree(n1)
printTree(cn1)