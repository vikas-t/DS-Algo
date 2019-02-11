#!/usr/bin/python

def partition(arr, l, r):
   i = l-1
   pivot = arr[r]
   for j in range(l, r):
      if arr[j] <= pivot:
         i = i + 1
         arr[j], arr[i] = arr[i], arr[j]
   arr[i+1], arr[r] = arr[r], arr[i+1]
   return i+1

def quickSort(arr, l, r):
   if l < r:
      p = partition(arr, l, r)
      quickSort(arr, l, p-1)
      quickSort(arr, p+1, r)
   return arr

def kSmallest(arr, l, r, k):
   """
   The idea is, not to do complete quicksort, but stop at the 
   point where pivot itself is k'th smallest element. Also, not to 
   recur for both left and right sides of pivot, but recur for one of 
   them according to the position of pivot. The worst case time 
   complexity of this method is O(n2), but it works in O(n) on average.
   """
   if k > 0 and k <= len(arr):
      # Remember that k is human readable so 1st smallest is the smallest of 
      # the array, there can be up to nth smallest where n is the len of array 
      p = partition(arr, l, r)
      if p == k - 1:
         return arr[p]
      elif p > k - 1:
         return kSmallest(arr, l, p-1, k)
      else:
         return kSmallest(arr, p+1, r, k)
   return -1

def sol(arr, l, r, k):
    n = len(arr)
    if k <=n and k > l:
        p = partition(arr, l, r)
        if p == n-k-1:
            return p
        elif p > n-k-1:
            return sol(arr, l, p-1, k)
        else:
            return sol(arr, p+1, r, k)


arr = [45, 23, 1, 0, 34, 97, 11, 8]
print quickSort(arr, 0, len(arr)-1)
print kSmallest(arr, 0, len(arr)-1, 8)