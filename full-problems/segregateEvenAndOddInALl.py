#/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/segregate-even-and-odd-nodes-in-a-linked-list/0

class LL:
    def __init__(self, head=None):
        self.head = head
    
    def addToLast(self, val):
        node = Node(val)
        tmp = self.head
        
        while tmp.next:
            tmp = tmp.next
        
        tmp.next = node
        node.next = None
    
    def print(self):
        ptr = self.head
        while ptr:
            print(ptr.val, end=" ")
            ptr = ptr.next
        print()

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = next

def segregate(head, n):
    ptr = head
    
    while ptr.next:
        ptr = ptr.next
    
    last = ptr
    ptr = head
    prev = None
    i=0
    
    while i<n and ptr:
        # If all the node values are odd it is going to be a infinite loop
        # so we keep track of the length evaluated so far and keep a 
        # condition over it
        nxt = ptr.next
        if ptr.val%2 != 0:
            # If the value is odd, push it to the last and make the next
            # of prev as the current one
            if prev == None:
                head = ptr.next
            elif ptr.next == None:
                pass
            # Special case if the last node's next is next, do not do anything
            else:
                prev.next = ptr.next
            last.next = ptr
            ptr.next = None
            last = ptr
            # Update the last node and mark the next of cur as None
        else:
            prev = ptr
        ptr = nxt
        i+=1
    return head

## Driver code
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    node0 = Node(arr[0])
    node0.next = None
    ll = LL(node0)
    
    for i in range(1, n):
        ll.addToLast(arr[i])
    
    ll.head=segregate(ll.head, n)
    ll.print()