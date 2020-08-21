# -*- coding: utf-8 -*-
"""
Created on Sun May  6 18:03:51 2018

@author: dms24081999
"""

n=int(input())
count=0
items=list(map(int,input().split()))
h=items[0]
for i in items:
    if i>h:
        h=i
for i in items:
    if i==h:
        count+=1
print(count)