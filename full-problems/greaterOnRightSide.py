#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/greater-on-right-side/0

def sol(arr, n):
    """
    Idea is to create a list which contains the max element till that index
    from the right
    """
    ml = [0]*(n)
    ml[n-1] = arr[n-1]
    
    for i in range(n-2, -1, -1):
        if arr[i] > ml[i+1]:
            ml[i] = arr[i]
        else:
            ml[i] = ml[i+1]
    
    for i in range(n-1):
        print(ml[i+1], end=" ")
    print(-1)

sol([16, 17, 4, 3, 5, 2], 6)