# -*- coding: utf-8 -*-
"""
Created on Sun May  6 13:47:42 2018

@author: dms24081999
"""
acount=0
bcount=0
a=list(map(int,input().split()))
b=list(map(int,input().split()))

for ai,bi in zip(a,b):
    if ai==bi:
        acount=acount+0
        bcount=bcount+0
    if ai>bi:
        acount=acount+1
    if ai<bi:
        bcount=bcount+1
print(str(acount)+" "+str(bcount))