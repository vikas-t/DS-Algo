#!/usr/bin/python3

# https://practice.geeksforgeeks.org/problems/stock-buy-and-sell/0

#code
def sol(arr):
    n = len(arr)
    buy = 0
    sell = 0
    isProfit = False
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            sell += 1
        else:
            if buy != sell:
                print("({} {})".format(buy, sell), end=" ")
                isProfit = True
            buy = i
            sell = i
    if buy != sell:
        print("({} {})".format(buy, sell), end=" ")
        isProfit = True
    if not isProfit:
        print("No Profit", end=" ")
    print()

arr=[23,13,25,29,33,19,34,45,65,67]
sol(arr)