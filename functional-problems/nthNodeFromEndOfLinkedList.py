#!/usr/bin/python
# https://practice.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1

def getNthFromLast(head, n):
    """
    Take two pointers one starting from head the other starting from the nth
    node, so when the latter node reaches the end the former would have reached
    the Lenth-n nodes
    """
    ptr = head
    
    c = 0
    while ptr and c < n:
        # We want the nptr to reach the last and not the None so we take
        # an extra step already thus the condition is c < n and not c < n-1
        ptr = ptr.next
        c+=1
    
    if c < n:
        return -1
    
    nptr=ptr
    ptr=head
    
    while nptr:
        ptr = ptr.next
        nptr = nptr.next
    return ptr.data