#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/binary-tree-to-dll/1

def BTToDLL(root):
    prev = [None]
    head = [None]
    # We keep the prev and head in a list so that they can be passed on 
    # as references
    btd(root, head, prev)
    return head[0]

def btd(root, head, prev):
    if root == None:
        return
    btd(root.left, head, prev)
    if prev[0] == None:
        head[0] = root
    else:
        prev[0].right = root
        root.left = prev[0]
    prev[0] = root
    btd(root.right, head, prev)