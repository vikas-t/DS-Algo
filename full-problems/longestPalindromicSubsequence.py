#!/usr/bin/python
# https://practice.geeksforgeeks.org/problems/longest-palindromic-subsequence/0

# substring is a continuous part or subpart of a string whereas subsequence 
# is the part of a string or sequence, that might be continuous or 
# not but the order of the elements is maintained

def sol(s, l, r):
    """
    The recursive approach
    """
    if r == l:
        return 1
    
    if r-l == 1 and s[l] == s[r]:
        return 2
    
    if r-l == 2 and s[l] == s[r]:
        return 3
    
    if s[l] == s[r]:
        return sol(s, l+1, r-1) + 2
    
    return max(
        sol(s, l, r-1), sol(s, l+1, r)
        )


def dp_sol(s):
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    
    for i in range(n-1):
        dp[i][i] = 1
        
    k = 2
    while k <= n:
        for i in range(n-k+1):
            l = i
            r = l + k - 1
            if s[l] == s[r] and k == 2:
                dp[l][r] = 2
            # The case with k == 2, gives the result only if it is calculated
            # inside the loop, when pre computed outside this loop, it
            # fails a test case, The test case is given below 
            elif s[l] == s[r]:
                dp[l][r] = dp[l+1][r-1] + 2
            else:
                dp[l][r] = max(dp[l+1][r], dp[l][r-1])
        k+=1
            
    return dp[0][n-1]

s = "webemkohvrmgoplzncygsqxzrtyhayvyewdqjtaekmnaeyzrbxzvqwwhqvqsvnrajwsupszbhmblmaepzgnrcjyueqpcdiepewjtrkwayxnlzraaznsexsydjphoxlddknydxudwrqjsjjtjznnyfndqdlfcwigixelxbotuecnonizovmmcbstedyjbirkgxvdymytqcigrqfgltunvmibpimtrddzbaezmeufgcnxsvffqavlmdpcobxffagicmjrqeywilvdibizdfmpldtzfqgmsmwvyfoqjmoszjvimfjplxhybaxirdwjpsgpxufhitbieystdbkqarobsnljqhuhzdyzzdiiyjqfjkymnifnavpujafzkzjjehielqmlbeqkoqzbbgodbfxmicmsdvdieompgadievusovvpbludrrrbvdtaayifmwwvwbdcxzwlvrcwdwbwptxkyskbqvidteysidufersziuynsbjhwgtxyfyrcgwwmuouzibfbthkpfzjijsfrlestcjvkfrybftcquhrqodhvdrgojlhxrbqtmnfrfdumwyetgwlwbssgjywvlgschkxuxcnefkteixzovknxcffofcjskbwrlvnkzbpglikthlkdvxcaejolnxdxabpnwcxvfobswomgzyjvxnxbwlmkirhksyxqdwlilobjeppepabmnypmjbytuffmgce"
print(dp_sol(s))