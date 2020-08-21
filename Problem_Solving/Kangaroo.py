# -*- coding: utf-8 -*-
"""
Created on Sun May  6 21:11:26 2018

@author: dms24081999
"""


kan=list(map(int,input().split()))
x1=kan[0]
v1=kan[1]
x2=kan[2]
v2=kan[3]
if (x1<x2 and v1<v2) or(x1>x2 and v1>v2):
    print("NO")
else:
    for i in range(0,10000):
        x1+=v1
        x2+=v2
        if x1==x2:
            print("YES")
            break
    if x1!=x2:
        print("NO")
