#!/usr/bin/python

# https://practice.geeksforgeeks.org/problems/count-all-possible-paths-from-top-left-to-bottom-right/0

def recSol(m, n):
   if m == 0 and n == 0:
      return 0
   
   return recSol(m-1, n) + recSol(m, n-1)

def dpSol(m,n):
   dp = []
   dp = [[0 for j in xrange(n)] for i in xrange(m)]
   
   for i in xrange(n):
      dp[0][i] = 1
   
   for i in xrange(m):
      dp[i][0] = 1

   for i in xrange(1,m):
      for j in xrange(1,n):
         dp[i][j] = dp[i-1][j] + dp[i][j-1]
   
   return dp[m-1][n-1]

print dpSol(3,3)

