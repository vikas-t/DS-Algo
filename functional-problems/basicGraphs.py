#!/usr/bin/python3

# Basic graph implementation in python3

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def dfsUtil(self, v, visited):
        visited[v] = True
        print(v, end=" ")

        for i in self.graph[v]:
            if not visited[v]:
                self.dfsUtil(i, visited)
    
    def dfs(self):
        """
        Traverses the graph depth wise even if the vertices are disjoint
        """
        v = [False]* len(self.graph)
        for i in range(v):
            if not visited[i]:
                self.dfsUtil(i, visited)
