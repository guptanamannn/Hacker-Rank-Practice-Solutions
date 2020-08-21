# -*- coding: utf-8 -*-
"""
Created on Tue May  8 10:52:01 2018

@author: dms24081999
"""

fn=[]
fns=0
nm=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for c in range(nm[0]):
    f=[]
    for item in range(a[nm[0]-1],b[nm[1]-nm[1]]+1):
        if (item%a[c]==0):
            f.append(item)
    fn.append(f)
    fns+=1
final=fn[0]
for i in range(0,fns):
    if i<fns:
        final=set(final).intersection(fn[i])

fn1=[]
fns1=0
final1=[]
for c in b:
    f1=[]
    for item in final:
        if c%item==0:
            f1.append(item)
    fn1.append(f1)
    fns1+=1
final1=fn1[0]
for i in range(0,fns1):
    if i<fns1:
        final1=set(final1).intersection(fn1[i])
len=0
for i in final1:
    len+=1
print(len)
