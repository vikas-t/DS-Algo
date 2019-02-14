#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.down = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.downEnd = head
        self.rightEnd = head
    
    def pushDown(self, val):
        node = Node(val)
        self.downEnd.down = node
        self.downEnd = node
    
    def pushRight(self, val):
        node = Node(val)
        self.rightEnd.right = node
        self.rightEnd = node
    
    def print(self):
        tmp = self.head
        while tmp:
            print(tmp.val, end=" ")
            tmp = tmp.right

def flatten(root):
    

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
