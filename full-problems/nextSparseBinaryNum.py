#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/next-sparse-binary-number/0

def sol(num):
    """
    By definition of sparse number two 1s cannot be adjacent but zeroes can be
    If two 1s are adjacent and we want to make a bigger number we cannot
    make the either of the bits 0, so only option left is we make the third
    bit 1 if it is 0 or we add an extra bit
    """
    b = list(bin(num)[2:])
    b.insert(0, "0")
    # We might have to add an extra bit lets add it. 
    # Adding a zero does not change the number
    
    #print(b)
    n = len(b)    
    i=n-2
    while i >= 1:
        # Search for the sequence where two adjacents bits are set and the
        # third bit to the left is not set and unset all the bits to its right
        # including both the set bits
        if b[i] == b[i+1] == "1" and b[i-1] == "0": 
            for j in range(i, n):
                b[j] = '0'
            b[i-1] = "1"
            # Set the third bit 
        i-=1

    num = 0
    n = len(b)
    #print(b)
    for i in range(n):
        p = n-1-i
        num += int(b[i])*(2**p)
    
    return num

print(sol(3))
print(sol(5))
print(sol(19169))
print(sol(18467))
print(sol(6334))

            
            