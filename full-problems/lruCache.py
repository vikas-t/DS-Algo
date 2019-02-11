#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/lru-cache/1

# Basic impl. of an LRU cache
"""
Least Recently Used (LRU): This cache algorithm keeps recently used items 
near the top of cache. Whenever a new item is accessed, the LRU places 
it at the top of the cache. When the cache limit has been reached, 
items that have been accessed less recently will be removed starting 
from the bottom of the cache.
We need the order in which the item was accessed and the access time must be
O(1). So an OrderedDict type seems perfect 
""" 

from collections import OrderedDict

class LruCache:
    def __init__(self, maxLen=100000):
        self.cache = OrderedDict()
        self.maxLen = maxLen
    
    def __setitem__(self, key, val):
        if k in self.cache:
            self.cache.pop(key)
        
        if len(self.cache) >= self.maxLen:
            self.cache.popitem(last=False)
        # Delete the value stored at last key, if length > maxLen
        # last = False imposes FIFO
        
        self.cache[key] = val
    
    def __getitem__(self, key):
        if key in self.cache:
            val = self.cache.pop(key)
            self.cache[key] = val
            # Delete the value when found, and add it again, this changes
            # the order, bringing the 'key' to the front thereby making
            # it the recently used   
            return val
        else:
            raise KeyError
# Usecase examples
x = LruCache()
x[1] = 2 # set
x[2] = 3 # set
y = x[1] # get