import sys

def sol(arr, n):
    """
    This is same as nextGreaterNumSetDigits
    """
    found = False
    for i in range(n-1, 0, -1):
        if arr[i-1] < arr[i]:
            found = True
            x = i-1
            break
    
    if not found:
        for i in range(n-1, -1, -1):
            print(arr[i], end=" ")
        return
    
    mn = sys.maxsize
    xm = None
    for i in range(x+1, n):
        if 0 < arr[i] - arr[x] < mn:
        # Careful with the difference zero and less than zero
            mn = arr[i] - arr[x]
            xm = i

    arr[x], arr[xm] = arr[xm], arr[x]
    tmp = arr[:x+1] + sorted(arr[x+1:])
    for x in tmp:
        print(x, end=" ")
    print()