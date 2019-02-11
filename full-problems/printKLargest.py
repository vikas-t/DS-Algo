#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/k-largest-elements/0


def partition(arr, l, r):
   i = l-1
   pivot = arr[r]
   for j in range(l, r):
      if arr[j] <= pivot:
         i = i + 1
         arr[j], arr[i] = arr[i], arr[j]
   arr[i+1], arr[r] = arr[r], arr[i+1]
   return i+1

def printKLargest(arr, k, l, r):
    n = len(arr)
    if k > 0 and k <= n:
        p = partition(arr, l, r)
        print("->")
        print(arr[l:p+1])
        print(arr[p+1:])
        if p == n-k-1:
            printArr(arr, p)
        elif p > n-k-1:
            printKLargest(arr, k, 0, p-1)
        else:
            printKLargest(arr, k, p+1, r)

def printArr(arr, p):
    tmpArr = sorted(arr[p+1:])
    for i in range(len(tmpArr)-1, -1, -1):
        if i:
            print(tmpArr[i], end=" ")
        else:
            print(tmpArr[i])
    
arr = [14,12,9,2,1,11,3,6,12,4]
k=5
printKLargest(arr, k, 0, len(arr)-1)