#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/number-to-words/0

tensToWords = {1000: "Thousand", 100: "Hundred"}
tens = {
    1: "Ten", 2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty",
    6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"}
ones = {
    1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six",  
    7: "Seven", 8: "Eight", 9: "Nine", 0: "Zero"}
tensP = {
    1: "Eleven" , 2: "Twelve", 3: "Thirteen", 4: "Fourteen", 
    5: "Fifteen", 6: "Sixteen" , 7: "Seventeen" , 8: "Eighteen" , 9: "Nineteen"
}

## check the spellings of 19 and 90

def sol(n):
    l = len(str(n))-1
    t = 10**l
    res = ""

    if n == 0:
        return ones[0]
    # Special case

    while n > 0:
        subRes = ""
        pv = n//t

        if t == 100 and n%t:
        # There is a connector and after hundred but only if something
        # follows
            conn = " and "
        else:
            conn = " "

        if t == 1:
            subRes = ones[pv]
        elif t == 10:
            if pv == 1 and n%t > 0:
            # To handle cases from 11-19
                subRes = tensP[n%t]
                n = 0
            # Set n as 0 because we do not want processing for ones from here on
            elif pv >= 1:
                subRes = tens[pv] + conn
        else:
            if pv >= 1:
                subRes = ones[pv] + " " + tensToWords[t] + conn
            # pv >= 1 is there to handle cases like 505, subRes goes empty
        
        res = res + subRes
        n = n%t
        t = t//10
    
    return res.strip()

nums = [10, 1000, 505, 36, 19, 2105, 1008, 100, 9999, 3037, 0]
for num in nums:
    print(sol(num))