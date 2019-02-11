#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/find-k-th-smallest-element-in-bst/1


def kthSmallestInBst(root, k):
    """
    We keep going left while pushing it on to the stack, The top of the stack
    is the smallest one. Pop the values from the stack one by one, if the value
    is not the desired one, push the left children of the right node in the 
    same way on the stack
    """

    stack = []
    while True:
        while root:
            stack.append(root.data)
            root = root.left

        root = stack.pop()
        if k == 1:
            return root.val
        else:
            root = root.right
            k -= 1