#!/usr/bin/python

# Longest increasing subsequence

import sys 

def longer_list(list1, list2):
   if len(list1) > len(list2):
      return list1
   else:
      return list2

def lis_rec(list, last=-1*sys.maxint):
   """
   Recursive solution
   """
   if not(list):
      return []
   
   incl = []
   if list[0] > last:
      incl = [list[0]] + lis_rec(list[1:], list[0])   
   excl = lis_rec(list[1:], last)

   return longer_list(incl, excl)


def lis_dp(list):
   n = len(list)
   dp = [[list[0]]] * n

   for i in xrange(1, n):
      for j in xrange(0, i):
         if list[i] > list[j] and len(dp[j]) + 1 > len(dp[i]):
            dp[i] = dp[j] + [list[i]]
      
   m = []
   for i in xrange(n):
      m = longer_list(m, dp[i])
      
   return m


def lis_dp2(arr):
   """
   Best solution
   """
   n = len(arr)
   dp = [1]*n
   for i in range(n):
      for j in range(i):
         if arr[j] <= arr[i]:
         # Watch out if = is not needed
            dp[i] = max(dp[i], dp[j]+1)
            # Max of included or excluded
   return max(dp)
   # dp can also be empty, you can return 0 in that case
   # Return the longest

test_cases = [
   [1, 10, 2, 11, 12],
   [15],
   [1, 2],
   [10, 2, 3, 19, 21, 90],
   [5, 4, 3, 2],
   [1, 2, 3, 4, 5, 6],
   [1, 15, 19, 2, 7, 14],
   [5,6, 7, 2, 3],
   [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
]

print lis_dp([1, 15, 19, 2])
print ""

for case_list in test_cases:
   print lis_dp(case_list)
   print lis_dp2(case_list)