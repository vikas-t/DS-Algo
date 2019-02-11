#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/unique-bsts/0
"""
Consider all possible binary search trees with each element at the root. 
If there are n nodes, then for each choice of root node, there are n – 1 
non-root nodes and these non-root nodes must be partitioned into those that 
are less than a chosen root and those that are greater than the chosen root.
Let’s say node i is chosen to be the root. Then there are i – 1 nodes smaller 
than i and n – i nodes bigger than i. For each of these two sets of nodes, 
there is a certain number of possible subtrees.
Let t(n) be the total number of BSTs with n nodes. The total number of BSTs 
with i at the root is t(i – 1) t(n – i). The two terms are multiplied 
together because the arrangements in the left and right subtrees are 
independent. That is, for each arrangement in the left tree and for each 
arrangement in the right tree, you get one BST with i at the root.
"""


def sol(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        for j in range(1, i+1):
            dp[i] += dp[j-1]*dp[i-j] 
    return dp[n]