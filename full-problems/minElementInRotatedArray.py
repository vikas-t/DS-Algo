#!/usr/bin/python

#https://practice.geeksforgeeks.org/problems/minimum-element-in-a-sorted-and-rotated-array/0

def findMin(arr, l, r):
    """
    If the first half is sorted, the pivot lies in the second half OR if the
    second half is sorted the pivot lies in the first half
    """
    if len(arr) == 1:
        return arr[0]
    
    mid = (l+r)//2
    while l<=r:
        print(arr[l], arr[mid], arr[r])
        if arr[mid+1] < arr[mid]:
            return arr[mid+1]
        # mid is the pivot, so mid+1 is the smallest
        if arr[mid-1] > arr[mid]:
            return arr[mid]
        # mid-1 is the pivot, so mid is the smallest
        
        elif arr[mid] > arr[l]:
            l = mid + 1
        else:
            r = mid - 1
        mid = (l+r)//2
    
    return arr[0]
    # If the array is completely sorted return the first one

arr = [335, 359, 383, 392, 422, 437, 448, 465, 468, 479, 492, 501, 539, 605, 668, 704, 706, 717, 719, 725, 727, 772, 812, 828, 870, 895, 896, 903, 913, 943, 962, 963, 996, 36, 146, 154, 170, 282, 293, 300, 323, 334]
arr = [18, 31, 47, 124, 165, 178, 183, 227, 228, 302, 304, 335, 367, 385, 399, 420, 424, 446, 494, 497, 533, 549, 558, 576, 577, 644, 663, 699, 703, 721, 742, 757, 761, 768, 773, 801, 810, 827, 897, 929, 981, 997]
print(findMin(arr, 0, len(arr)-1))