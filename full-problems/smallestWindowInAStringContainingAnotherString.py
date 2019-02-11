#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string/0

import sys

def sol(mstr, pat):
    hashStr = {}
    hashPat = {}
    
    if len(pat) > len(mstr):
        return -1
    
    for x in pat:
        hashPat[x] = hashPat[x] + 1 if x in hashPat else 1
    # Store the occurence of pattern string in a hash
    
    count = 0
    b = 0
    bi = -1
    minLen = sys.maxsize
    
    for i in range(len(mstr)):
        x = mstr[i]
        hashStr[x] = hashStr[x] + 1 if x in hashStr else 1
        # Store the occurence of main string in a hash
        
        if x in hashStr and x in hashPat and hashStr[x] <= hashPat[x]:
            count+=1
        # If the character is present in both the hashmaps update the count
        
        if count == len(pat):
        # Check that all characters in the pattern are found in the main string
            ch = mstr[b]
            while (ch not in hashPat) or (ch in hashPat and hashStr[ch] > hashPat[ch]):
                # Keep eliminating characters from the left by increasing the
                # start counter (which is b here) if the character is not found
                # in the pattern string
                # OR
                # If the character is found in the pattern string but there 
                # are more occurences in the main string, we will chose the 
                # other character that comes after to minimise the window
                if ch in hashPat and hashStr[ch] > hashPat[ch]:
                    hashStr[ch] -= 1
                b+=1
                ch = mstr[b]

            lw = i - b +1
            if minLen > lw:
                minLen = lw
                bi = b
            # Update the start and the window len if a window is found smaller
            # than the minimum length
    
    if bi == -1:
        return -1
    return mstr[bi:minLen+bi]

print(sol("timetopractice", "toc"))
print(sol("zoomlazapzo", "oza"))