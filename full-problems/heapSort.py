#!/usr/bin/python

def heapify(arr, n, i):
   """
   Converting the tree in to a Max. Heap
   """
   largest = i
   left = 2*i + 1
   right = 2*i + 2

   for s in [right, left]:
      if s < n and arr[s] > arr[largest]:
         largest = s

   if largest != i:
      arr[i], arr[largest] = arr[largest], arr[i]
      heapify(arr, n, largest)  

def heapSort(arr):
   n = len(arr)
   for i in xrange(n/2-1,-1,-1):
      heapify(arr,n,i)

   for i in xrange(n-1, -1, -1):
      arr[i], arr[0] = arr[0], arr[i]
      heapify(arr, i, 0)
   
   return arr
   

arr = [12, 19, 34, 1, 66, 74, 59, 13, 21]
arr2 = [13, 35, 9, 91, 9, 20, 18, 14, 70, 4]
print heapSort(arr)
print heapSort(arr2)
