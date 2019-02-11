#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/length-of-the-longest-substring/0

def sol(s):
    n = len(s)
    start = 0
    end = 0
    h = {}
    m = 0
    
    for i in range(n):
        if s[i] in h and h[s[i]] >= start:
        # If the current char already exists in the substring that 
        # we are considering, update the start and the end
                m = max(m, end-start+1)
                start = h[s[i]] + 1
        h[s[i]] = i
        # Keep a count in a hash
        end = i
        m = max(m, end-start+1)
    return m

print(sol("ashdfkjahdjkfbbnmbuicae"))
print(sol("geeksforgeeks"))
print(sol("qwertqwer"))
print(sol("abc"))
print(sol("qwertyuioijhghmnbvcdswwazxcv"))