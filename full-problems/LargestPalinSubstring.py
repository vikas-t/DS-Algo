#!/usr/bin/python3

# Largest palindrome sustring in a string

def largestPanlinSub(arr):
    """
    If we use the naive solution which is checking every susbtring for 
    max. palindromic substring, the complexity becomes n3.
    Now, coming to this solution the time complexity is n2 but the space 
    complexity is also n2. Clearly, we need a better solution
    """
    n = len(arr)
    sol = [[False for _ in range(n)] for _ in range(n)]

    maxlen = 1
    s = 0

    for i in range(n):
        sol[i][i] = 1
    
    l = 0
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            sol[i][i+1] = True
            l = 2
            if l > maxlen:
                s = i
                maxlen = l
    
    for k in range(3, n+1):
        l = 0
        for i in range(0, n-k+1):
            j = i+k-1
            if arr[i] == arr[j] and sol[i+1][j-1]:
                sol[i][j] = True
                l = k
                if l > maxlen:
                    s = i
                    maxlen = l
    return arr[s:s+maxlen]


def sol(arr):
    """
    Time complexity n2
    Space complexity 1
    It uses two while loops, because you need diff. 'l' and 'r' for 
    calculating palindromic string. Ex: aba, abba
    """
    n = len(arr)
    l = 0
    s = 0
    maxlen = 1
    
    for i in range(1, n):
        l = i-1
        r = i
        while l>=0 and r<n and arr[l] == arr[r]:
            ln = r - l + 1
            if ln > maxlen:
                maxlen = ln
                s = l
            l = l - 1
            r = r + 1
    
        l = i-1
        r = i+1
        while l>=0 and r<n and arr[l] == arr[r]:
            ln = r - l + 1
            if ln > maxlen:
                maxlen = ln
                s = l
            l = l - 1
            r = r + 1
    
    return arr[s: s+maxlen]


strs = ["abc", "cc", "abbc", "adedc", "aaaabbaa", "ssttayyya", "fyfvladzpbfudkklrwq", "bbabcbcab"]
for s in strs:
    print(largestPanlinSub(s))