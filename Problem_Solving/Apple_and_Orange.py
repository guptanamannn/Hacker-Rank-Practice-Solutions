# -*- coding: utf-8 -*-
"""
Created on Mon May  7 10:56:27 2018

@author: dms24081999
"""
st=list(map(int,input().split()))
ab=list(map(int,input().split()))
mn=list(map(int,input().split()))
ma=list(map(int,input().split()))
nb=list(map(int,input().split()))
counta=0
countb=0

maposit=[]
nbposit=[]
for i in ma:
    maposit.append(int(i+ab[0]))
for i in nb:
    nbposit.append(int(i+ab[1]))
for i in maposit:
    if i in range(st[0],st[1]+1):
        counta+=1
for i in nbposit:
    if i in range(st[0],st[1]+1):
        countb+=1
print(counta)
print(countb)