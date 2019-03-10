#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/leaves-to-dll/1

# In the question it is asked to remove the leaf nodes in the tree and 
# add it in the DLL from left to right
# The conversion goes inplace, so we use the same Node where left is previous
# in the DLL and right is the next node

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Dll:
    def __init__(self, head):
        self.head = head
    
    def printList(self):
        tmp = self.head
        while tmp:
            print(tmp.data, end=" ")
            tmp = tmp.right
        print()

def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print(root.data, end=" ")
    inOrder(root.right)

def extractLeaves(root, head=None, cur=None):
    """
    We traverse from left to right keeping a reference of the head node
    and the current node, when we encounter the leaf node we update the 
    current node pointers and return the root as None thereby unlinking it
    from the tree
    Another appraoch is to traverse the tree from right to left and build
    the DLL from right to left
    https://www.geeksforgeeks.org/connect-leaves-doubly-linked-list/
    """
    if root == None:
        return root, head

    if cur == None and head == None:
        head = [Node(None)]
        cur = [head[0]]
        # We need a reference of this nodes so we keep them in a list
        # In the beginning make a dummy Node as the start and make the same
        # as the current

    if root.left == None and root.right == None:
        node = Node(root.data)
        cur[0].right = node
        node.left = cur[0]
        cur[0] = node
        return None, head
    
    root.left, head = extractLeaves(root.left, head, cur)
    root.right, head = extractLeaves(root.right, head, cur)
    return root, head

# Driver code
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

n1.left = n2
n1.right = n3

n2.left = n4
n2.right = n5

n3.left = n6

#inOrder(n1)
#print()
_,head = extractLeaves(n1)
# We can also make 'head' as global and keep referring it accross the 
# recursion
head = head[0].right
# The first node was a dummy so move a node right
dll = Dll(head)

dll.printList()
inOrder(n1)
# Verify that the tree is updated as well