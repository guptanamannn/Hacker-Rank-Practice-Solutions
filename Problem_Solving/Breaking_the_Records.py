# -*- coding: utf-8 -*-
"""
Created on Mon May  7 15:55:24 2018

@author: dms24081999
"""

n=int(input())
score=list(map(int,input().split()))
low=high=score[0]
worst=0
best=0
bw=[]
for item in score:
    bw.append(item)
for item in score:
    if item<high:
        worst+=1
        high=item
    elif item>low:
        best+=1
        low=item
print(best, worst)
