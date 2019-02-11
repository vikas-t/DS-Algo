#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/longest-distinct-characters-in-string/0

def sol(arr):
    """
    Naive solution. Complexity is n^2
    """
    n = len(arr)
    s = 0
    m = 0
    while s < n:
        st = s
        c = 0
        h = {}
        while st < n:
            if arr[st] in h:
                break
            else:
                h[arr[st]] = 1
                c += 1
            st += 1
        m = max(c, m)
        s += 1
    return m

def sol2(arr):
    """
    This comes out of the editorial. Complexity is n
    """
    n = len(arr)
    v = [-1 for i in range(256)]
    m = 1
    clen = 1
    v[ord(arr[0])] = 0
    
    for i in range(1, n):
        lastIndex = v[ord(arr[i])]
        
        if lastIndex == -1 or i-clen > lastIndex:
            clen+=1
        else:
            m = max(m, clen)
            clen = i - lastIndex
        v[ord(arr[i])] = i
    
    m = max(m, clen)
    
    return m

def sol3(arr):
    n = len(arr)
    
    h = {}
    maxlen= 1
    clen = 1
    
    h[arr[0]] = 0
    for i in range(1, n):
        if arr[i] not in h or i - clen > h[arr[i]]:
            clen+=1
        else:
            maxlen = max(maxlen, clen)
            clen = i - h[arr[i]]
        h[arr[i]] = i
        
    maxlen = max(maxlen, clen)
    return maxlen
