#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def printList(self):
        tmp = self.head

        while tmp:
            print(tmp.data, end=" ")
            tmp = tmp.next
        print()
    
    def getLast(self):
        tmp = self.head
        while tmp and tmp.next:
            tmp = tmp.next
        
        return tmp
    
    def getCount(self):
        tmp = self.head
        c = 0
        while tmp:
            tmp = tmp.next
            c+=1
        return c

def sortList(ll):
    """
    !! This is not correct. Careful !
    """
    last = ll.getLast()
    n = ll.getCount()
    cur = ll.head
    head = ll.head
    prev = None

    c = 0

    while cur and c < n:
        if cur.data == 0 and cur != head:
            prev.next = cur.next
            cur.next = head
            head = cur
            cur = prev.next
        elif cur.data == 2:
            prev.next = cur.next
            cur.next = None
            last.next = cur
            last = cur
        else:
            prev = cur
            cur = cur.next
        c += 1
    return head

    
## Driver code
ll = LinkedList()
n1 = Node(0)
n2 = Node(2)
n3 = Node(1)
n4 = Node(0)
n5 = Node(0)
n6 = Node(1)
n7 = Node(2)
n8 = Node(1)

ll.head = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8

ll.printList()
ll.head = sortList(ll)
#ll.printList()