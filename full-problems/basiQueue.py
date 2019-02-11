#!/usr/bin/python3

# Basics of Queue data structure

import Queue

class queue:
    def __init__(self):
        self.q = []
    
    def get(self):
        return self.q.pop(0)
    
    def put(self, v):
        self.q.append(v)
    
    def isEmpty(self):
        return self.q == []

q = Queue.Queue(maxsize=10)
q.put(10)
q.put(15)
q.put(1)

print(q.empty())
print(q.get())
# Fetch 1st element
print(q.get())
# Fetch 2nd
print(q.empty())
# Check if empty
print(q.get())
# Fetch 3rd element
print(q.empty())

#print(q.get(block=False))
# This does not block and raises Exception if the Q is empty

q = queue()
q.put(10)
q.put(15)
q.put(1)

print(q.isEmpty())
print(q.get())
# Fetch 1st element
print(q.get())
# Fetch 2nd
print(q.isEmpty())
# Check if empty
print(q.get())
# Fetch 3rd element
print(q.isEmpty())



