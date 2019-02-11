#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/top-k-numbers/0

def sol(arr, n, k):
    f = {0:0}
    rl = [0]*(k+1)
    # Lets initialise a list of k+1 elements
    # We have taken one extra element here so as we dont overwrite an existing
    # result or subresult 
    
    for x in arr:
        f[x] = f[x] + 1 if x in f else 1
        
        rl[k] = x
        # Store the newest element at the last meaning at position which
        # has the least frequency
        i = rl.index(x)
        i-=1
        # Find the position where the element occurs for the first time so 
        # as to adjust the elements preeceding that. The elements in 
        # succession remains unchanged
        
        while i >= 0:
            if f[rl[i]] < f[rl[i+1]]:
                rl[i], rl[i+1] = rl[i+1], rl[i]
            # If the element to the left has smaller frequency, swap it
            elif f[rl[i]] == f[rl[i+1]] and rl[i] > rl[i+1]:
                rl[i], rl[i+1] = rl[i+1], rl[i]
            # If the number to the left has same frequency but the number is
            # greater swap it
            else:
                break
            # No point going further to the left
            i-=1
        
        for r in rl[:k]:
            if not r:
                continue
            print(r, end=" ")
        # Print the results as asked in the question
    print()