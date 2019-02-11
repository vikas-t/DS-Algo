#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/decode-the-pattern/0

def lookAndSaySequence(n):
    """
    https://en.wikipedia.org/wiki/Look-and-say_sequence

    As the name suggests look and say the previous no.
    111221 is read off as "three 1s, two 2s, then one 1" or 312211 which
    becomes the next number of the sequence
    """
    seq = [0, 1]
    num = "1"
    
    for _ in range(n):
        l = len(num)
        tmp = ""
        i=0
        
        while i < l:
            cnt = 0
            j = i
            while j < l and num[j] == num[i]:
                # Count till the digit differs
                cnt+=1
                j+=1
            tmp += str(cnt) + num[i]
            i = j
            # Append the frequency and digit in the result and update the 
            # next iteration of the loop
        num = tmp
        # The result becomes the next no. of the sequence
        seq.append(num)
    
    return seq

seq = lookAndSaySequence(21)
# Calculate all till the given range
for _ in range(int(input())):
    n = int(input())
    print(seq[n])