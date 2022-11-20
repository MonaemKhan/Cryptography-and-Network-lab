from array import *
import numpy as np


def AHP(arr):
    n = len(arr)

    summ = [0 for i in range(n)]

    x = 0
    while x < n:
        for i in range(n):
            summ[x] = summ[x] + arr[i][x]
        x = x + 1

    for i in range(n):
        for j in range(n):
            arr[i][j] = arr[i][j] / summ[j]

    weight = [0 for i in range(n)]
    for i in range(n):
        for j in range(n):
            weight[i] = arr[i][j] + weight[i]
        weight[i] = weight[i] / n
    return weight

goal_arr = [[1,3,5],[0.33,1,2],[0.2,0.5,1]]
w_c = AHP(goal_arr)

max = 0
index = 0
for i in range(len(goal_arr)):
    per = w_c[i]*100
    if max < per:
        max = per
        index = i
    print("For Criteria-"+str(i+1)+" Priority Is : %.3f"%per+"%")

print("After applying AHP we can say that Criteria-"+str(index+1)+" is best for us")