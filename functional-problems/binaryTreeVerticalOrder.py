#!/usr/bin/python

class Node:
   def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None

def getVerticalOrder(root, hd, m):
   if root is None:
      return
   
   if hd not in m:
      m[hd] = []

   m[hd].append(root.data)

   getVerticalOrder(root.left, hd-1, m)
   getVerticalOrder(root.right, hd+1, m)

def printVerticalOrder(root):
   hd = 0
   m = {}
   getVerticalOrder(root, hd, m)
   for index, value in enumerate(sorted(m)):
      for i in m[value]:
         print i,
      print

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)
printVerticalOrder(root)