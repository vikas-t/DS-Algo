# Question #1

def find_all_paths(graph, start, end, path=[]):
   path = path + [start]
   if start == end:
      return [path]
   if not graph.has_key(start):
      return []
   paths = []
   for node in graph[start]:
      if node not in path:
         newpaths = find_all_paths(graph, node, end, path)
         for newpath in newpaths:
            paths.append(newpath)
   return paths

n,m = map(int, (raw_input().strip().split()))

r = []
for i in xrange(n+1):
   r.append([0]*(n+1))

for i in xrange(m):
   n1, n2, rt = map(int,(raw_input().strip().split()))
   r[n1][n2] = rt

graph = {}
tx = []
for i in xrange(n+1):
   for j in xrange(n+1):
      if r[i][j] or r[j][i]:
         if i not in graph:
            graph[i] = []
         graph[i].append(j)

for i in xrange(1,n+1):
   for j in xrange(1,n+1):
      if i == j:
         continue
      x = find_all_paths(graph,i,j)
      for path in x:
         tx.append(tuple(path))

rtx = set(tx)
print rtx
print ""
print tx