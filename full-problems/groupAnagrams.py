#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/k-anagrams-1/0

def sol(s, n):
    gr = {}
    for i in range(n):
        x = ''.join( c for c in sorted(s[i]))
        # Sort every word and put it in a hash with count increasing
        gr[x] = gr[x] + 1 if x in gr else 1
    
    for r in sorted(gr.values()):
        print(r, end=" ")
    print()