#code
import sys

def sol(arr, n):
    """
    The complexity here is n^2
    """
    b = [-1]*n
    prev = -1
    for i in range(n-1):
        if not arr[i]:
            b[i] = prev
            continue
        
        j = i + 1
        mv = -1
        m = None
        while j < n and arr[i] > arr[j]:
            if arr[j] > mv:
                mv = arr[j]
                m = j
            j+=1
        
        if j == n:
            b[i] = m
        else:
            b[i] = j
        prev = b[i]
    print(b)

    c = 0
    i = 0
    while i < n and i!=-1:
        j = b[i]
        lb = arr[i]
        for k in range(i+1, j+1):
            d = min(lb, arr[j]) - arr[k]
            print(d)
            if d > 0 and lb >= arr[k]:
                c += d
        i = j
    return c

def sol2(arr, n):
    """
    Pre compute the left and the right boundaries of the array element. The
    diff. b/w the element value and the smaller of the boundary will be the
    units of water stored
    """
    lb = [0]*n
    rb = [0]*n
    
    lb[0] = arr[0]
    for i in range(1, n):
        lb[i] = max(lb[i-1], arr[i])
    
    rb[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        rb[i] = max(rb[i+1], arr[i])
    
    c = 0
    for i in range(n):
        c += min(lb[i], rb[i]) - arr[i]
    return c

arr = [7, 4, 0, 9]
print(sol(arr, len(arr)))