# -*- coding: utf-8 -*-
"""
Created on Mon May  7 16:16:24 2018

@author: dms24081999
"""
n=int(input())
s=list(map(int,input().split()))
dm=list(map(int,input().split()))
prob=0
for count,j in enumerate(s):
    add=0
    for i in range(0,dm[1]):
        if count+i<n:
            add=add+s[count+i]
    if add==dm[0]:
        prob+=1
print(prob)