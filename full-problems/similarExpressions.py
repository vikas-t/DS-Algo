#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/similar-expressions/0

"""
The solution is broken in to two parts Simplify and Compare
The simplify removes part removes the all the brackets and adds a Sign for 
every character
The compare part creates a hash count where if the Sign is plus the count is 
increased, decreased otherwise
If the hashes are equal we return True 
"""

def signExp(expression, sign):
    """
    Opens the brackets, depending upon the Sign
    """
    arr = list(expression)
    if sign == "-":
        for i in range(len(expression)):
            # Invert the sign if the 'sign' is '-'
            if arr[i] == "+":
                arr[i] = "-"
            elif arr[i] == "-":
                arr[i] = "+"
    # If the first characters is not a sign, it is a '+' and we need to 
    # add it to the subexpression
    if arr[0] != "+" and arr[0] != "-":
        arr.insert(0, sign)
    return "".join(x for x in arr)  

def simplify(expression):
    """
    Keep pushing characters on to a stack till a ")" is collected. Once it is
    collected we keep popping from the stack till a "("  is obtained. 
    We then pop the sign which is either the next top of the stack or we 
    take it as a "+"
    We open the brackets and push the result on top of the stack again
    Finally, pop all the characters and join the subexpressions to create
    the simplified expression
    """
    q = []
    for x in expression:
        if x != ")":
            q.append(x)
        else:
            subexp = ""
            while q:
                #print(q)
                c = q.pop()
                if c == "(":
                    if len(q) and (q[-1] == "+" or q[-1] == "-"):
                            sign = q.pop()
                    else:
                        sign = "+"
                    subexp = signExp(subexp, sign)
                    q.append(subexp)
                    break
                else:
                    subexp = c + subexp
    exp = ""
    while q:
        c = q.pop()
        exp = c + exp
    
    if len(exp) and exp[0] != "+" and exp[0] != "-":
    # Again if the first character is not a 'sign' make it a "+"
        exp = "+" + exp
    
    return exp

def getHash(expression):
    """
    Create a hash of all characters for an expression, every character has
    a sign prefixed, so we decrease the count of character if its a '-' else
    we keep increasing. We remove the characters if their count is zero
    """
    h = {}
    for i in range(0, len(expression), 2):
        sign = expression[i]
        char = expression[i+1]
        if char not in h:
            h[char] = 0
        if sign == "+":
            h[char] += 1
        else:
            h[char] -= 1
        if h[char] == 0:
            del h[char]
    return h

def sol(exp1, exp2):
    a = simplify(exp1)
    b = simplify(exp2)
    #print(a, b)
    ha = getHash(a)
    hb = getHash(b)
    #print(ha, hb)
    return ha == hb
    
print(sol("c-(a-(b+c))+a-b", "c+c"))
print(sol("-(a+b+c)", "a-b-c"))
print(sol("a-b-(c-d)", "a-b-c-d"))
print(sol("a-b-(c-d)", "a-b-c+d"))
print(sol("d+b-(c+d)", "a-a+b-c"))
print(sol("(((a+b+c)))", "a+b+c"))