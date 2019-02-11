#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1

def isPalindrome(head):
    """
    The standard stack solution.
    There is also a method via recursion that did not work
    """
    stack = []
    ptr = head
    
    while ptr:
        stack.append(ptr.data)
        ptr=ptr.next
    
    ptr = head
    while ptr:
        stackTop = stack[-1]
        if stackTop != ptr.data:
            return False
        else:
            stack.pop()
        ptr = ptr.next
    return True
    