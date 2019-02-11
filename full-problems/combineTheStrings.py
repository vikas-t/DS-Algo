#!/usr/bin/python

#https://practice.geeksforgeeks.org/problems/combine-the-strings/0

def sol(arr):
    bb = 0
    rr = 0
    br = 0
    rb = 0
    
    for i in arr:
        if i[0] == 'R' and i[-1] == 'R':
            rr+=1
        elif i[0] == 'B' and i[-1] == 'B':
            bb+=1
        elif i[0] == 'R' and i[-1] == 'B':
            rb+=1
        elif i[0] == 'B' and i[-1] == 'R':
            br+=1
        
    min_br = 2*min(br, rb)
    if br == 0 and rb == 0:
        cs = max(bb, rr)
    elif br == rb:
        cs = bb + rr + 2*min_br
    else:
        cs = bb + rr + 2*min_br + 1
    
    if cs == 1:
        return 0
    else:
        return cs*len(arr[0])

