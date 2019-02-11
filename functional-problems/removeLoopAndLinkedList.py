#!/usr/bin/python3
# https://www.geeksforgeeks.org/detect-and-remove-loop-in-a-linked-list/

def detectLoop(head):
    ptr = head
    dptr = head
    
    while ptr and dptr and dptr.next:
        ptr = ptr.next
        dptr = dptr.next.next
        if ptr == dptr:
            return ptr
        # Return the node where the two nodes meet, basically  the nodes
        # are supposed to meet at the loop node
    return False

def removeTheLoop(head):
    loopPtr = detectLoop(head)
    
    if not loopPtr:
        return 1
        
    ptr = head
    while ptr:
        if ptr.next == loopPtr:
            ptr.next = loopPtr.next
            return 1
        ptr = ptr.next