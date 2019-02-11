#!/usr/bin/python3
#https://practice.geeksforgeeks.org/problems/roman-number-to-integer/0

romanMap = {
    1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"
}

numMap = {
    "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
}
def numToRom(n):
    l = len(str(n)) - 1
    t = 10**l
    res = ""
    
    while n > 0:
        subRes = ""
        pv = n//t
        if pv == 1 or pv == 5:
            subRes = romanMap[t*pv]
        elif pv == 2 or pv == 3:
            subRes = romanMap[t]*pv
        elif pv == 4:
            subRes = romanMap[t] + romanMap[5*t]
        elif 6 <= pv <= 8:
            subRes = romanMap[5*t] + romanMap[t]*(pv-5)
        elif pv == 9:
            subRes = romanMap[t] + romanMap[10*t]
        # The else part falls for 0 where subRes is ""
        
        res = res + subRes
        n = n%t
        t = t//10
    
    return res

def romToNum(s):
    l = len(s)
    i = 0
    n = 0
    while i < l:
        if i+1 < l and numMap[s[i+1]] > numMap[s[i]]:
        # If the next roman character is greater than the current the value
        # is subtracted, else in all cases we add up the values
                n = n + numMap[s[i+1]] - numMap[s[i]]
                i+=1
        else:
            n = n + numMap[s[i]]
        i+=1
    return n

for num in [110, 101, 50, 1408, 9, 996, 40, 3999, 1]:
    x = numToRom(num)
    print num, x, romToNum(x)