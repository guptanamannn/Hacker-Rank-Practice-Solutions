# -*- coding: utf-8 -*-
"""
Created on Sun May  6 17:34:42 2018

@author: dms24081999
"""
sums=[]
sg=[]
items=list(map(int,input().split()))
for i,val1 in enumerate(items):
    sum=0
    for j,val2 in enumerate(items):
        if i!=j:
            sum=sum+val2
    sums.append(sum)

s=sums[0]
g=sums[0]
for i in sums:
    if i<s:
        s=i
    if i>g:
        g=i
print(str(s)+" "+str(g))
