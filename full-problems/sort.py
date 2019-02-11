#!/usr/bin/python

# Sorting algorithms

def selection_sort(arr):
   l = len(arr)   
   
   for i in xrange(l):
      mini = i
      for j in xrange(i+1, l):
         if arr[j] < arr[mini]:
            mini = j
      
      arr[i], arr[mini] = arr[mini], arr[i]
   return arr

def insertion_sort(arr):
   n = len(arr)

   for i in xrange(1,n):
      flag = False
      for j in xrange(i):
         if arr[i] < arr[j]:
            s = arr[i]
            flag = True
            break
      
      if not flag:
         continue
      
      for m in xrange(i-1, j-1, -1):
         arr[m+1] = arr[m]
      
      arr[j] = s
   return arr

def insertion_sort2(arr):
   n = len(arr)
   for i in xrange(n):
      s = -1
      p = arr[i]
      for j in xrange(i-1, -1, -1):
         if p < arr[j]:
            arr[j+1] = arr[j]
            s = j
      if s > -1:
         arr[s] = p
   return arr

def counting_sort(arr, k):
   #import pdb; pdb.set_trace()
   l = len(arr)
   c = [0]*k

   for i in arr:
      c[i] += 1

   for i in xrange(1, k):
      c[i] += c[i-1]

   for i in xrange(k-1, 0, -1):
      c[i] = c[i-1]
   
   c[0] = 0

   r = [0]*l

   for i in arr:
      r[c[i]] = i
      c[i] += 1
   
   return r

print selection_sort([3, 12, 90, 1, 0, 65, 19, 73])
print selection_sort([-1, 78, -3, -1, -1])
print "\n\n"
print insertion_sort2([3, 12, 90, 1])
print insertion_sort2([-1, 78, -3, -1, -1])
print "\n\n"
print counting_sort([7, 2, 1, 4, 4, 1, 8], 9)
print counting_sort([13, 2, 0, 9, 11, 3, 6, 2, 2, 7], 14)