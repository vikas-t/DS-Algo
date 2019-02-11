#!/usr/bin/python3
# https://practice.geeksforgeeks.org/problems/maximum-product-subarray/0
def sol(arr, n):
    mxth = 1
    mnth = 1
    res = 1
    for i in range(n):
        if arr[i] > 0:
            mxth = mxth*arr[i]
            mnth = min(mnth*arr[i], 1)
        elif arr[i] < 0:
            tmp = mxth
            mxth = max(mnth*arr[i], 1)
            mnth = tmp*arr[i]
        else:
            mxth = 1
            mnth = 1
        res = max(res, mxth)
    return res
    