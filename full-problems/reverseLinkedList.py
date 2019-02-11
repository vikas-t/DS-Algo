#!/usr/bin/python

# Reversing a linked list

class Node:
   def __init__(self, data):
      self.data = data
      self.next = None

class LinkedList:
   def __init__(self):
      self.head = None
   
   def push(self, val):
      """
      Insert a node at the end
      """
      node = Node(val)
      node.next = None
      tmp = self.head
      
      if not self.head:
         self.head = node
         return

      while tmp.next:
         tmp = tmp.next
      tmp.next = node
   
   def reverseList(self):
      current = self.head
      prev = None
      next = None

      while current:
         next = current.next
         current.next = prev
         prev = current
         current = next
      self.head = prev
   
   def printList(self):
      tmp = self.head
      while tmp:
         print tmp.data, 
         tmp = tmp.next
      print ""

ll = LinkedList()
for i in [4, 1 , 3, 7, 9]:
   ll.push(i)

ll.printList()

ll.reverseList()
ll.printList()
   