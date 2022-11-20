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

def Alter_Max(arr):
    max = 0
    index = 0
    for i in range(len(arr)):
        per = int(arr[i]*100)
        if max < per :
            max = per
            index = i
        print("For Alternative-" + str(i + 1) + " Priority Is : " + str(per) + "%")
    return index

def AHP_fun():
    goal_arr = [[1,3,5],[0.33,1,2],[0.2,0.5,1]]
    print("-------Criteria Table wirh respect to Goal---------")
    for x in goal_arr:
        print(x)
    w_c = AHP(goal_arr)
    print()
    q=1
    for i in w_c:
        print("Criteria-%d Weights : "%q, end=" ")
        print("%.3f"%i)
        q+=1
    print()
    Alter_arr = [[[1,2,5],[0.5,1,2],[0.2,0.5,1]],
                [[1,5,2],[0.2,1,0.33],[0.5,3,1]],
                [[1,0.5,0.33],[2,1,0.5],[3,2,1]]]
    q = 1
    for x in Alter_arr:
        print("--------Alternate Table With Respect to Criteria-"+str(q)+"--------")
        for y in x:
            print(y)
        q+=1
        print()
    print()

    Alter_weight = []
    Alter_weight_old = []

    for x in Alter_arr:
        Alter_weight.append(AHP(x))
        Alter_weight_old.append(AHP(x))


    w=1
    for x in Alter_weight_old:
        print("With Respect To Criteria-%d"%w)
        print("===================")
        q = 1
        for i in x:
            print("Alternet Weight-%d : "%q, end=" ")
            print("%.3f"%i)
            q += 1
        w+=1
        print()


    j = 0
    for x in Alter_weight:
        for i in range(len(x)):
            x[i] = x[i]*w_c[j]
        j=j+1

    print("Multy Criteria Decission Table")
    print("=====================")
    for x in Alter_weight:
        print("[",end=" ")
        for i in x:
            print("%.3f"%i,end=" ,")
        print("]")
    print()

    Alter_weight_final = [0 for i in range(len(goal_arr))]
    for x in Alter_weight:
        for i in range(len(x)):
            Alter_weight_final[i] += x[i]
    print("Final Decission Table")
    print("==============")

    index = Alter_Max(Alter_weight_final)
    max = 0
    ind = 0
    k=0
    for x in Alter_weight_old:
        per = int(x[index]*100)
        if max < per :
            max = per
            ind = k
        k+=1
    print("After applying AHP we can say that Alternative-" + str(index + 1) + " is best for us")

AHP_fun()