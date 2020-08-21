# -*- coding: utf-8 -*-
"""
Created on Mon May  7 21:27:57 2018

@author: dms24081999
"""
money=[]
flavors=[]
cost=[]

nvisits=int(input())
for i in range(0,nvisits):
    money.append(int(input()))
    flavors.append(int(input()))
    cost.append(list(map(int,input().split())))

for i in range(0,nvisits):
    for a,item1 in enumerate(cost[i]):
        for b,item2 in enumerate(cost[i]):
            if a!=b:
                item=item1+item2
                if item==money[i]:
                    s=b+1
                    j=a+1
    print(s, j)