#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/right-view-of-binary-tree/1


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrder(root):
    if root == None:
        return
    inOrder(root.left)
    print(root.data, end=" ")
    inOrder(root.right)

def getRightViewSum(root):
    h = {}
    level = 0
    getSum(root, level, h)
    return sum(h.values())

def getSum(root, level, h):
    """
    Time complexity is O(n) and space complexity is O(h) where h is 
    the height of the tree
    """
    if root == None:
        return
    
    h[level] = root.data
    
    getSum(root.left, level+1, h)
    getSum(root.right, level+1, h)

def getSum2(root, level=0, maxLevel=None, sum=None):
    """
    This approach is better than the previous one as it does not use extra 
    space. We keep track of two variables as references, maxlevel and sum.
    maxLevel refers to the highest level reached so far. sum is the total sum
    of the right view uptil that level. We traverse right child first, so
    as we go down the level we obtain the rightmost node of the level. We 
    compare the level with maxLevel and if it is greater signifies that 
    we have obtained the rightmost node of a that level, we add the node 
    data to the sum. Finally we return the sum on level 0.
    """
    if root == None:
        return 0
    
    if maxLevel == None:
        maxLevel = [-1]
        sum = [0]
    
    if  maxLevel[0] < level:
        sum[0] += root.data
        maxLevel[0] = level
    
    getSum2(root.right, level+1, maxLevel, sum) 
    getSum2(root.left , level+1, maxLevel, sum)

    if level == 0:
        return sum[0]

nodes = [None]
for v in range(1, 9):
    nodes.append(Node(v))

nodes[1].left = nodes[2]
nodes[1].right = nodes[3]

nodes[2].left = nodes[4]
nodes[2].right = nodes[5]

nodes[3].left = nodes[6]
nodes[3].right = nodes[7]

nodes[4].right = nodes[8]

#inOrder(nodes[1])
print(getRightViewSum(nodes[1]))
print(getSum2(nodes[1]))