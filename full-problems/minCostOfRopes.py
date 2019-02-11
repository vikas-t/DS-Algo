#!/usr/bin/python3
#https://practice.geeksforgeeks.org/problems/minimum-cost-of-ropes/0

def sol(arr, n):
    """
    The most straight forward soln
    sort the array and reduce the element from 3rd till last
    Add the sum of first two in front and again sort the array
    """
    arr.sort()
    s=0
    while len(arr)>1:
        x=arr[0]+arr[1]
        arr=arr[2:]
        arr.insert(0,x)
        s+=arr[0]
        arr.sort()
    return s

def sol2(arr, n):
    """
    Same solution using heap/priority queue
    Uses min heap
    """
    import heapq as h
    h.heapify(arr)
    s = 0
    i = 0
    while i < n-1:
        # The last element gets added to the sum when last two are added
        # So we need not go to the last element
        m1 = h.heappop(arr)
        m2 = h.heappop(arr)
        t = m1 + m2
        h.heappush(arr, t)
        s = s + t
        i+=1
    print(s