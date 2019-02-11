#!/usr/bin/python

class Node:
   def __init__(self, data):
      self.data = data
      self.prev = None
      self.next = None

class dll:
   def __init__(self):
      self.head = None
   
   def push(self, data):
      node = Node(data)
      node.next = self.head
      
      if self.head:
         self.head.prev = node
      
      self.head = node
   
   def insertAfter(self, prev, data):
      if not prev:
         return
      
      node = Node(data)

      node.next = prev.next
      node.prev = prev

      prev.next = node

      if node.next:
         node.next.prev = node
      
   
   def append(self, data):
      node = Node(data)
      
      tmp = self.head

      while tmp.next:
         tmp = tmp.next
      
      tmp.next = node
      node.next = None
      node.prev = tmp
   

   def printList(self):
      tmp = self.head
      
      while tmp:
         print tmp.data,
         last = tmp
         tmp = tmp.next
      print 
      
      while last:
         print last.data,
         last = last.prev
   

ll = dll()

ll.push(4)
ll.push(5)
ll.push(7)
ll.append(1)
ll.append(3)

ll.printList()