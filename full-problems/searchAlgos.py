#!/usr/bin/python

from math import sqrt

def binary_search(arr, x):
   l = len(arr)
   start = 0
   end = l - 1
   mid = l/2

   while l:
      if x == arr[mid]:
         return mid
      elif x < arr[mid]:
         end = mid - 1
      else:
         start = mid + 1
      l = end - start + 1
      #mid = l/2 + start
      mid = (start + end)/2
   
   return -1

def jump_search(arr, x):
   l = len(arr)
   m = int(sqrt(l))
   k = m 
   pk  = 0
   while k < l:
      if arr[k] == x:
         return k
      if arr[k] > x:
         break
      pk = k
      k += m
   
   k = min(k, l-1)

   for i in xrange(pk, k+1):
      if arr[i] == x:
         return i
   
   return -1 


arrs = ([1,2,5,8,11,18,19], [1])
#print binary_search(arrs[0], 8)
#print binary_search(arrs[1], 1)
print binary_search([1,2], 5)

# print jump_search(arrs[0], 8)
# print jump_search(arrs[1], 3)
# print jump_search(arrs[0], 2)
