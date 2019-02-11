#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/huffman-encoding/0

class btree():
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
    
    def add(self, val):
        print("New node", val)
        if not self.data:
            self.data = val
            return
        
        root = btree(self.data)
        while root:
            if val < root.data:
                if not root.left:
                    root.left = btree(val)
                else:
                    root = self.left
            else:
                if not root.right:
                    root.right = btree(val)
                else:
                    root = self.right

def huffman(root, code=""):
    if not root:
        print(code)
        return
    huffman(root.left, code+"0")
    huffman(root.right, code+"1") 

def sol(frq):
    import heapq
    heapq.heapify(frq)
    t = btree(None)
    
    while frq:
        m1 = heapq.heappop(frq)
        m2 = heapq.heappop(frq)
        heapq.heappush(frq, m1+m2)
        heapq.heapify(frq)
        t.add(m1+m2)
    
    print(huffman(t))
    
frq = list(map(int, "5 9 12 13 16 45".split()))
sol(frq)