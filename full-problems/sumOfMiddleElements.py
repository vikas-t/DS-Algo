#!/usr/bin/python
#https://practice.geeksforgeeks.org/problems/sum-of-middle-elements-of-two-sorted-arrays/0
def sol(a, b, n):
    """
    Because the two arrays are sorted apply the merge strategy, and keep
    the counts, now total elements in the new array should be equal 
    to i+j (k in this case).
    Check if k is n/2 or n/2-1 element
    """
    i = 0
    j = 0
    k = 0
    s = 0
    while i < n and j < n:
        if a[i] <= b[j]:
            if k == (2*n)//2 or k == ((2*n)//2)-1:
                s+=a[i]
            i+=1
        else:
            if k == 2*n//2 or k == (2*n//2)-1:
                s+=b[j]
            j+=1
        k+=1
    
    #If the first array is all smaller than the second array, in that case
    #only one element will be added to the sum before the loop breaks.
    #So add the first element of the the other loop
    if i == 0:
        s = s+b[0]
    elif j == 0:
        s = s+a[0]
    return s 