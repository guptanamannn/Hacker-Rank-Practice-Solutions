# -*- coding: utf-8 -*-
"""
Created on Mon May  7 16:44:39 2018

@author: dms24081999
"""

nk=list(map(int,input().split()))
a=list(map(int,input().split()))
out=0

for i,val1 in enumerate(a):
    for j,val2 in enumerate(a):
        if i<j:
            val=val1+val2
            if val%nk[1]==0:
                out+=1
print(out)