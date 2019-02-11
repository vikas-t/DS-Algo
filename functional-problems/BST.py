#!/usr/bin/python3

# Binary tree impl

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self,val):
        if val < self.data:
            if self.left:
                self.left.insert(val)
            else:
                self.left = Node(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = Node(val)

    def inOrder(self):
        if self.left:
            self.left.inOrder()
        if self.data:
            print(self.data, end=" ")
        if self.right:
            self.right.inOrder()

# Driver code

root = Node(10)
for v in [3, 5, 11, 6, 2, 9, 8]:
    root.insert(v)
root.inOrder()
