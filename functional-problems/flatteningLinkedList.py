#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1

class Node:
    def __init__(self, data):
        self.val = data
        self.right = None
        self.down = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.downEnd = None
        self.rightEnd = None
    
    def pushDown(self, val):
        self.downEnd = self.downEnd or self.head
        
        node = Node(val)
        self.downEnd.down = node
        self.downEnd = node
    
    def pushRight(self, val):
        self.rightEnd = self.rightEnd or self.head

        node = Node(val)
        self.rightEnd.right = node
        self.rightEnd = node
        self.downEnd = node
        # We first update all the down nodes going down and then we move right, 
        # Once we move right we update the right most node as the new down end    
    
    def printList(self):
        """
        For every node print the nodes that are connected downwards, 
        then move right and so on
        """
        tmp = self.head
        
        while tmp:
            tmpD = tmp
            hasDown = False
            while tmpD:
                hasDown = True
                print(tmpD.val, end="v")
                tmpD = tmpD.down
            if not hasDown:
                print(tmp.val, end=" ")
            print(" -> ", end=" ")
            tmp = tmp.right

def merge(a, b):
    if a == None:
        return b
    
    if b == None:
        return a
    
    result = None
    
    if a.val < b.val:
        result = a
        result.down = merge(a.down, b)
    else:
        result = b
        result.down = merge(a, b.down)
    
    return result

def flatten(root):
    if root == None or root.right == None:
        return root
    
    return merge(root, flatten(root.right))

# Driver code
# We intend to create the following linked list

"""
    5 -> 10 -> 19 -> 28
    |    |     |     |
    V    V     V     V
    7    20    22    35
    |          |     |
    V          V     V
    8          50    40
    |                |
    V                V
    30               45
"""

ll = LinkedList()
ll.head = Node(5)
ll.pushDown(7)
ll.pushDown(8)
ll.pushDown(30)

ll.pushRight(10)
ll.pushDown(20)

ll.pushRight(19)
ll.pushDown(22)
ll.pushDown(50)

ll.pushRight(28)
ll.pushDown(35)
ll.pushDown(40)
ll.pushDown(45)

ll.printList()
print()

flatten(ll.head)
ll.printList()