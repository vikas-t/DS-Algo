#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/detect-loop-in-linked-list/1

def detectLoop(head):
    """
    Take two pointers one that moves one step, the other moves two steps
    if at any point both meet its a loop
    Imagine it in a form of circle, where the first pointer completes half the
    second has completed one full cycle. Again when the first completes
    one half the other completes the full cycle and they meet where 
    they started.

    The other solution is to keep a map of visited nodes and return True
    if we found a node that is already visited
    """
    f = head
    s = head
    
    while f and s and s.next:
        f = f.next
        s = s.next.next
        if f == s:
            return True
    return False