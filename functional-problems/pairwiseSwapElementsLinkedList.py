#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/pairwise-swap-elements-of-a-linked-list-by-swapping-data/1

def pairWiseSwap(head):
    """
    We dont need to change the references just swap the values of the next
    and the current node  
    """
    ptr = head
    while ptr and ptr.next:
        ptr.data, ptr.next.data = ptr.next.data, ptr.data
        ptr = ptr.next.next
    return head