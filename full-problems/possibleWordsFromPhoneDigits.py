#!/usr/bin/python3
#https://practice.geeksforgeeks.org/problems/possible-words-from-phone-digits/0

def sol(n, N, arr, r=[]):
    """
    Standard backtracking. Recurse through all and keep printing at the end
    """
    if n == N:
        print("".join(x for x in r), end=" ")
        return
    k = arr[n]
    for i in range(len(keyMap[arr[n]])):
        r.append(keyMap[arr[n]][i])
        sol(n+1, N, arr, r)
        r.pop()

keyMap = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
N=3
arr=[2,3,4]
sol(0, N, arr)
print()