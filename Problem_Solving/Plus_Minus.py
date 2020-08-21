# -*- coding: utf-8 -*-
"""
Created on Sun May  6 15:24:50 2018

@author: dms24081999
"""

n=input()
pn=0
nn=0
zn=0
items=list(map(int,input().split()))
for i in items:
    if i>0:
        pn=pn+1
    elif i==0:
        zn=zn+1
    else:
        nn=nn+1
print(round(float(pn)/float(n),6))
print(round(float(nn)/float(n),6))
print(round(float(zn)/float(n),6))