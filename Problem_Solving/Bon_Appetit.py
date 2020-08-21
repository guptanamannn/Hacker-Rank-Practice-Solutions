# -*- coding: utf-8 -*-
"""
Created on Mon May  7 17:55:04 2018

@author: dms24081999
"""
nk=list(map(int,input().split()))
k=nk[1]
bill=list(map(int,input().split()))
charged=int(input())
sum=0
for i,item in enumerate(bill):
    if i!=k:
        sum=sum+item
div=sum/2
if charged>div:
    print(int(charged-div))
else:
    print("Bon Appetit")
