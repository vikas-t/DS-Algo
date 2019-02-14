#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/reverse-a-linked-list/1

def reverseList(self):
    # Code here
    if self.head is None:
        return None
    
    prev = self.head
    ptr  = self.head
    
    while ptr and ptr.next:
        tmp = ptr.next
        ptr.next = tmp.next
        tmp.next = prev
        prev = tmp
    self.head = prev
    return self.head