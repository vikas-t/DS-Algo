#!/usr/bin/python 

# Basic examples of binary trees

class Node:
   def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
   
   def insert(self, data):
      if self.data:
         if data < self.data:
            if not self.left:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data > self.data:
            if not self.right:
               self.right = Node(data)
            else:
               self.right.insert(data)
      else:
         self.data = data
      
   def printTree(self):
      if self.left:
         self.left.printTree()
      if self.data:
         print self.data,
      if self.right:
         self.right.printTree()

root = Node(10)
root.insert(11)
root.insert(14)
root.insert(7)
root.insert(8)
root.insert(0)

root.printTree()

