#!/usr/bin/python

# https://www.geeksforgeeks.org/minimum-length-unsorted-subarray-sorting-which-makes-the-complete-array-sorted/

import sys

def mlua(arr):
   n = len(arr)

   i = 0
   while i < n-1 and arr[i+1] > arr[i]:
      i+=1
   s=i

   i = n-1
   while i > 0 and arr[i] > arr[i-1]:
      i=i-1
   e=i

   min_e = arr[s]
   max_e = arr[s]
   idx_min = s
   idx_max = s
   
   for i in xrange(s, e+1):
      if arr[i] < min_e:
         min_e = arr[i]
         idx_min = i
      
      if arr[i] > max_e:
         max_e = arr[i]
         idx_max = i
   
   i=idx_min-1
   while i>=0 and arr[i] >= min_e:
      i = i-1
   le = i+1

   i=idx_max+1
   while i < n and arr[i] <= max_e:
      i=i+1
   re = i-1

   print le, re
   

   
arr = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
arr2 = [0, 1, 15, 25, 6, 7, 30, 40, 50]
arr3 = [475,134,392,201,355,491,198,420,281,79,432,45,341,488,400,26,484,39,493,194,253,12,61,335,341,498,286,30,41,306,292,393,211,50,79,480,472,278,74,194,121,498,327,277,291,83,79,160,419,490,160,450]
#mlua(arr)
#mlua(arr2)
mlua(arr3)






# def mlua(arr):
#    n = len(arr)

#    i = 0
#    while i < n-1 and arr[i+1] > arr[i]:
#       i+=1
#    s=i

#    i = n-1
#    while i > 0 and arr[i] > arr[i-1]:
#       i=i-1
   
#    if i == n-1:
#        print (0, n-1)
#        return
#    e=i

#    min_e = arr[s]
#    max_e = arr[s]
#    idx_min = s
#    idx_max = s
   
#    for i in range(s, e+1):
#       if arr[i] < min_e:
#          min_e = arr[i]
#          idx_min = i
      
#       if arr[i] > max_e:
#          max_e = arr[i]
#          idx_max = i
   
#    i=idx_min-1
#    while i>=0 and arr[i] > min_e:
#       i = i-1
#    le = i+1

#    i=idx_max+1
#    while i < n and arr[i] < max_e:
#       i=i+1
#    re = i-1

#    print(le, re)

# for _ in range(int(input())):
#     n = int(input())
#     arr = list(map(int, input().strip().split()))
#     mlua(arr)
    
    