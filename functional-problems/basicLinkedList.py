#!/usr/bin/python

# Basics of Linked List

class Node:
   def __init__(self, data):
      self.data = data
      self.next = None

class LinkedList():
   def __init__(self):
      self.head = None
   
   def printList(self):
      tmp = self.head
      while tmp:
         print tmp.data,
         tmp = tmp.next
      print 
   
   def insertAtbegin(self, val):
      x = Node(val)
      self.head = x
      x.next = e1
   
   def insertAtEnd(self, val):
      x = Node(val)
      tmp = self.head
      while tmp.next:
         tmp = tmp.next
      tmp.next = x
      x.head = None
   
   def insertAtPos(self, node, val):
      if not node:
         print "Cannot be added"
      
      x = Node(val)
      tmp = node.next
      node.next = x
      x.next = tmp
   
   def delete(self, val):
      tmp  = self.head
      while tmp:
         if tmp.data == val: 
            break
         prev = tmp
         tmp = tmp.next
      
      prev.next = tmp.next

list1 = LinkedList()
e1 = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
e4 = Node("Thurs")

list1.head = e1
e1.next = e2
e2.next = e3
e3.next = e4

list1.printList()

list1.insertAtbegin("Sun")
list1.printList()

list1.insertAtEnd("Fri")
list1.printList()

list1.insertAtPos(e2, "Tue2")
list1.printList()

list1.delete("Tue2")
list1.printList()


#### IMPORTANT ###
# If you copy one Node to other and change the actual object itself, the value
# is going to reflect in the copied object as well
# Ex:  Copy e1 to tmp, modify e1.next this will bring a change in tmp.next
tmp = e1
print(e1.data, e1.next.data, tmp.data,tmp.next.data)
e1.next = e3
print(e1.data, e1.next.data, tmp.data,tmp.next.data)