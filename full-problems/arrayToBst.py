#!/usr/bin/python3

# https://practice.geeksforgeeks.org/problems/array-to-bst/0

from math import floor

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def getBst(arr, l, r):
    if l > r:
        return None
    mid = l+((r-l)//2)
    # In the question it says floor(n/2) which does not work for all cases
    root = Node(arr[mid])
    root.left = getBst(arr, l, mid-1)
    root.right = getBst(arr, mid+1, r)
    return root

def preOrder(r):
    if not r:
        return
    print(r.data, end=" " )
    preOrder(r.left)
    preOrder(r.right)


for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    r = getBst(arr, 0, n-1)
    preOrder(r)
    print()