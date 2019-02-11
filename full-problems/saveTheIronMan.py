#!/usr/bin/python
# https://practice.geeksforgeeks.org/problems/save-ironman/0

def sol(s):
    n = len(s)
    #print(s[0], s[-1])
    l = 0
    r = n-1
    while l < r:
        lv = False
        rv = False
        cl = s[l].lower()
        cr = s[r].lower()
        
        if cl.isdigit() or cl.isalpha():
            lv = True
        
        if cr.isdigit() or cr.isalpha():
            rv = True
        
        if lv and rv:
            if cl != cr:
                return False
            l+=1
            r-=1
        elif not rv:
            r-=1
        else:
            l+=1
    
    return True

