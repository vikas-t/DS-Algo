#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1

def findMid(head):
    """
    Start two pointers, one that moves a step, the other takes two steps
    When the other reaches end the first will be in the mid
    Works for both even and odd lengths
    """
    ref = head
    ptr = head
    while ptr and ref and ref.next:
        ptr = ptr.next
        ref = ref.next.next
    return ptr