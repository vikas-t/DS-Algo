#!/usr/bin/python

# Question - Count the path 
# https://www.hiredintech.com/classrooms/algorithm-design/lesson/12/task/15

def dp_ctp(grid):
   """
   Dynamic approach
   """
   m = 0 # Row count
   n = 0 # Column count

   try:
      while grid[m]:
         m = m + 1
   except:
      pass
   
   n = len(grid[0])
   dp = [0]*m

   for i in xrange(m):
      dp[i] = [0]*n
   # Initailise solution list
   
   dp[0][n-1] = 1
   
   for i in xrange(m):
      for j in xrange(n-1, -1, -1):
         l = j - 1 
         d = i + 1
         # We traverse from from down and left to get a bottom up list

         if l > -1 and grid[i][l] == '0':
            dp[i][l] = dp[i][l] + dp[i][j]
         
         if d < m and grid[d][j] == '0':
            dp[d][j] = dp[d][j] + dp[i][j]
   return dp[m-1][0]%1000003


def count_the_paths(grid):
   """
   Best solution
   """
   mod = 1000003
   dp = [0]*len(grid[0])
   for row in reversed(xrange(len(grid))):
      for col in xrange(len(grid[0])):
         if grid[row][col] == '1':
            dp[col] = 0
         elif col != 0:
            dp[col] = (dp[col] + dp[col-1])%mod
         elif row == len(grid)-1:
            dp[col] = 1
   return dp[-1]

def rec_ctp(grid, x, y, m, n):
   """
   Recursive approach
   """
   if x == 0 and y == n - 1:
      return 1

   if x < 0 or y > n-1:
      return 0

   if grid[x][y]:
      return 0

   return (rec_ctp(grid, x-1, y, m, n) + rec_ctp(grid, x, y+1, m, n))%1000003

x = [['0', '0', '0'], ['0', '0', '0'], ['0','0','0']]
#x = [['0'],['0']]
print dp_ctp(x)
# print rec_ctp(x, 2, 0, 3, 3)