#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/find-median-in-a-stream/0

#code
import heapq

def getMedian(e, mxhp, mnhp):
    mx = -1*mxhp[0]
    # Get the top of the maxheap
    if e < mx:
        heapq.heappush(mxhp, -1*e)
    else:
        heapq.heappush(mnhp, e)
    # If the given element is smaller than maxheap push it to the maxheap
    # else push it to the minheap
    
    lmx = len(mxhp)
    lmn = len(mnhp)
    
    if lmx > lmn + 1:
        x = -1*heapq.heappop(mxhp)
        heapq.heappush(mnhp, x)
        lmx -= 1
        lmn += 1
    elif lmn > lmx + 1:
        x = heapq.heappop(mnhp)
        heapq.heappush(mxhp, -1*x)
        lmn -= 1
        lmx += 1
    # If the length of one of the heap is greater than the other by more than
    # 1 we pop the element from the bigger heap and push it to the other heap
    # Also adjust the lenths of both the heaps
    
    if lmx > lmn:
        return -1*mxhp[0]
    elif lmn > lmx:
        return mnhp[0]
    else:
        return (mnhp[0] + (-1*mxhp[0]))//2
    # If length of both the heaps are same, return the average of their 
    # top elements, otherwise return the top if the larger heap
        
for i in range(int(input())):
    e = int(input())
    if i == 0:
        print(e)
        f = e
    # For the first element, the element is the median
    elif i == 1:
        print((f+e)//2)
        mxhp = []
        mnhp = []
        if f < e:
            mxhp.append(-1*f)
        # We are using the negative of a minheap to obtain a maxheap here
            mnhp.append(e)
        else:
            mnhp.append(f)
            mxhp.append(-1*e)
        # If there are two elements push the smaller one to maxheap and the 
        # other one to minheap
        heapq.heapify(mxhp)
        heapq.heapify(mnhp)
    else:
        x = getMedian(e, mxhp, mnhp)
        print(x)
        
        