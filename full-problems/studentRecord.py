#!/usr/bin/python3
#https://practice.geeksforgeeks.org/problems/student-record/0

def sol(records, n):
    mx = 0
    res = []
    for ni in range(0, n*4, 4):
        am = sum(map(int, records[ni+1:ni+4]))//3
        if am > mx:
            # If we find a better average overwrite the result list
            # with the name of the student and the average
            mx = am
            res = [(records[ni], am)]
        elif am == mx:
            # If the averages are same append in the result list
            res.append((records[ni], am))
    for name, marks in res:
        print(name, end=" ")
    print(marks)
    # print the result as stated in the problem