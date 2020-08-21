# -*- coding: utf-8 -*-
"""
Created on Sat May  5 22:34:56 2018

@author: dms24081999
"""
n=input()
items=list(map(int,input().split()))
add=0
for item in items:
    add=add+item
print(add)
