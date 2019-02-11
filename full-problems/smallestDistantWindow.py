#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/smallest-distant-window/0

def sol(s):
    """
    From both ends check the character that is occurring only once
    ! This is failing one test case
    """
    n = len(s)
    h = {}
    for x in s:
        h[x] = h[x]+1 if x in h else 1
    
    hc = dict(h)

    start = 0
    end = n-1

    while start < n and h[s[start]] > 1:
        h[s[start]]-=1
        start+=1

    while end > -1 and h[s[end]] > 1:
        h[s[end]]-=1
        end-=1 
    
    m1 = end-start+1
    
    start = 0
    end = n-1

    while end > -1 and hc[s[end]] > 1:
        hc[s[end]]-=1
        end-=1

    while start < n and hc[s[start]] > 1:
        hc[s[start]]-=1
        start+=1
    
    m2 = end-start+1
    return min(m1, m2)

def sol2(s):
    """
    The correct solution
    """
    v = {}
    count = 0
    for x in s:
        if x not in v:
            count+=1
            v[x] = True
    
    dc = 0
    start = 0
    ml = len(s)
    h = {}
    for i in range(len(s)):
        if s[i] in h:
            h[s[i]] = h[s[i]] + 1
        else:
            dc+=1
            # Count the distinct characters
            h[s[i]] = 1
        
        if dc == count:
            while h[s[start]] > 1:
                h[s[start]] -= 1
                start+=1
            # If we have repeated characters shift the start to its right
            # and decrease the occurrence count by 1
            l = i-start+1
            if l < ml:
                ml = min(ml, l)
                si = start
    print(si)
    return ml

#print(sol2("aabcbcdbca"))
#print(sol2("aab"))
#print(sol2("aaabbaacc"))
#print(sol2("wwaakwyprxnxpypjgtlhfteetxbafkrejsfvrenlebjtccgjvrsdowiixlidxdiixpervseavnwypdinwdrlacvanhelk"))
print(sol2("ejdinmujtyxiddmoqvysajhexyeewjqduvliiiuchumnxccqxdjanrensktrvmuqigctpwxyrnmppogpurpilwxe"))
#print(sol2("abcaabbc"))