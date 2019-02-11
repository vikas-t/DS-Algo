#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/next-smallest-palindrome/0

def nextPalin(arr, n):
    carry = 0
    if n%2 == 0:
        lli = n//2-1
        rfi = n//2
        hi = n//2-1
    else:
        lli = n//2-1
        rfi = n//2+1
        hi = n//2
    # lli -> left last index i.e the last index of left half
    # rfi -> right first index i.e first index of the right half
    # hi is the half index i.e the index from where the mirroring begins 
    # from the half. If the length is even it begins from the lli whereas
    # when length is even the int(n/2) is included is common 
    
    ilg = False
    # ilg -> is left greater
    l = lli
    r = rfi
    while l >= 0:
        if arr[l] > arr[r]:
            ilg = True
            break
        elif arr[l] < arr[r]:
            break
        l-=1
        r+=1
    # Check if the left part is greater than the other half
        
    carry = 0    
    if not ilg:
        carry = 1
        for i in range(hi, -1, -1):
            tmp = arr[i] + carry
            arr[i] = tmp%10
            carry = tmp//10
        # Add 1 to the first half where the mirroring starts from the middle
    if carry:
        arr.insert(0, 1)
    
    l = 0
    r = n-1
    while l < r:
        arr[r] = arr[l]
        l+=1
        r-=1
    # Copy the first half as the second half to mirror
    
    return " ".join(str(x) for x in arr)

def sol(num):
    """
    There are 5 cases
    1. If the number is a single digit then we add 1 and return
    2. If all the digits are 9 then the first and last are ones and the rest 
       are zeroes or adding two the no. Ex: 99+2 = 101
    3. The left half of the number is greater than the second half wherein
       we just copy the left to the right to make a palindrome
    4. If the left half is smaller than the right half in that case we 
       add 1 to the right most digit of the left half and mirror the same
    5. If the no. is already a palindrome we follow the same as done in 4
       Ex: 1221 -> 1331
    """
    arr = list(map(int, num))
    n = len(arr)

    if len(arr) == 1 and arr[0] != 9:
        arr[0]+=1
        return " ".join(str(x) for x in arr)
    # case 1
    
    all9 = True
    for i in range(n):
        if arr[i] != 9:
            all9 = False
            break

    if all9:
        for i in range(n):
            arr[i] = 0
        arr.insert(0, 1)
        arr[-1] = 1
        return " ".join(str(x) for x in arr)
    # case 2
    
    return nextPalin(arr, n)
    # nextPalin covers the rest of the cases

cases = ["12311", "999", "9", "7621", "8279", "111", "191", "34566512", "34566598"]
for case in cases:
    print(sol(case))



