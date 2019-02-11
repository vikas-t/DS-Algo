#!/usr/bin/python3
#https://practice.geeksforgeeks.org/problems/three-great-candidates/0
def sol(arr, n):
    """
    We pick the smallest two, multiplying gives them a positive. The third
    number has to be always positive to we take the largest one. so multiplying
    these 3 can give the max and the obvious are the 3 largest. So we pick the
    max among the two
    """
    arr = sorted(arr)
    return max(arr[-1]*arr[-2]*arr[-3], arr[0]*arr[1]*arr[-1])