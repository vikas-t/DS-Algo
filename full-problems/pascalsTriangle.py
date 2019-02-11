#!/usr/bin/python3
# Pascal's Triange

n=6
p = [[1], [1, 1]]
for i in range(2, n):
    p.append([1 for _ in range(i+1)])
    for j in range(1, i):
        p[i][j] = p[i-1][j] + p[i-1][j-1]
print(p)