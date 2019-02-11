#!/usr/bin/python

# Longest common subsequnce between two arrays

def lcs(x, y):
    """
    Dynamic approach
    """
    m = len(x)
    n = len(y)
    dp = []
    # Note that dp[i][j] represents solution for strings with 'length' i and j 
    for i in xrange(m+1):
        dp.append([])
        for j in xrange(n+1):
            dp[i].append(0)
    
    for i in xrange(1, m+1):
        for j in xrange(1, n+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]


def recursiveLcs(x, y):
    if not len(x) or not len(y):
        return 0
    
    if x[0] == y[0]:
        return 1 + recursiveLcs(x[1:], y[1:])
    else:
        return max(recursiveLcs(x[1:],y), recursiveLcs(x, y[1:]))


print recursiveLcs('AEDFHR', 'ABCDGH')
print recursiveLcs('RANDOM', 'ANDOM')
print recursiveLcs('CAT', 'TAC')
print recursiveLcs('TEST', 'PQW')

print lcs('AEDFHR', 'ABCDGH')
print lcs('RANDOM', 'ANDOM')
print lcs('CAT', 'TAC')
print lcs('TEST', 'PQW')