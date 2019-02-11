#!/usr/bin/python3

# https://practice.geeksforgeeks.org/problems/next-larger-element/0


class stack:
    def __init__(self):
        self.s = []
    
    def push(self, val):
        self.s.append(val)
    
    def pop(self):
        return self.s.pop()
    
    def isEmpty(self):
        return self.s == []

def sol(arr, n):
    stack = []
    res = [-1]*n
    
    for i in range(n):
        if not stack:
            stack.append(i)
            continue
        
        top = stack[-1]
        while stack and arr[i] > arr[top]:
            e=stack.pop()
            res[e] = arr[i]
            if stack:
                top = stack[-1]
        stack.append(i)
    
    for x in res:
        print(x, end=" ")
    print()
