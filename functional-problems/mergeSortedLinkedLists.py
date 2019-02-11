#!/usr/bin/python
# https://practice.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1


class Node:
    def __init__(self, data=None):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def print(self):
        ptr = self.head
        while ptr:
            print(ptr.data, end=" ")
            ptr = ptr.next
        print()

def mergeSortedLL(a, b):
    if a is None:
        return b
    if b is None:
        return a

    s = t = Node()
    # Create a dummmy node
    # While t keeps moving forward s will keep a track of the beginning
    while a and b:
        if a.data < b.data:
            c = a
            a = a.next
        else:
            c = b
            b = b.next
        t.next = c
        t = t.next
    t.next = a or b
    return s.next

# Driver code
ll1 = LinkedList()
n1 = Node(2)
n2 = Node(3)
n3 = Node(20)
ll1.head = n1
n1.next = n2
n2.next = n3


ll2 = LinkedList()
n4 = Node(5)
n5 = Node(10)
n6 = Node(15)
ll2.head = n4
n4.next = n5
n5.next = n6

m = mergeSortedLL(n1, n4)
ll3 = LinkedList()
ll3.head = m
ll3.print()