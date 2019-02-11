#!/usr/bin/python3

def dpED(x, y):
    m = len(x)
    n = len(y)

    dp = []
    for i in xrange(m+1):
        dp.append([])
        for j in xrange(n+1):
            dp[i].append(0)
            if i == 0:
                dp[i][j] = j
            if j == 0:
                dp[i][j] = i
    
    for i in xrange(1,m+1):
        for j in xrange(1,n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i][j-1], # Insert
                    dp[i-1][j], # Remove
                    dp[i-1][j-1] # Replace
                )
    
    return dp[m][n]
# Assume problem statements with strings str1 -> length m and str2 -> length n
# Now if we insert a character in str1 to make the last character same, 
# the problem statement reduces to string with length m and n-1 because last
# character is now same
# Similarily, when we 'Replace', the last character becomes same and the 
# problem statement reduces to strings with length  m-1 and n-1 


def recED(x, y, m, n):
    if not m:
        return n
    if not n:
        return m
    
    if x[m-1] == y[n-1]:
        return recED(x, y, m-1, n-1)
    
    return min(
            1 + recED(x, y, m-1, n),
            1 + recED(x, y, m, n-1),
            1 + recED(x, y, m-1, n-1)
        )
print dpED('sunday', 'saturday')
print recED('sunday', 'saturday', len('sunday'), len('saturday'))