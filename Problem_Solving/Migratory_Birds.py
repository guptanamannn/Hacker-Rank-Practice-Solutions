# -*- coding: utf-8 -*-
"""
Created on Mon May  7 16:58:28 2018

@author: dms24081999
"""

#n=int(input())
#ar=list(map(int,input().split()))
#hbirds=[]
#birds=[]
#views=[]
#for item in ar:
#    k=0
#    for rep in ar:
#        if rep == item:
#            k=k+1
#    birds.append(item)
#    views.append(k)
#high=0
#for h in views:
#    if h>high:
#        high=h
#        
#for i,h in enumerate(views):
#    if h==high and birds[i] not in hbirds:
#        hbirds.append(birds[i])
#small=hbirds[0]
#for item in hbirds:
#    if item<small:
#        small=item
#print(small)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
a = ar.count(1)
b = ar.count(2)
c = ar.count(3)
d = ar.count(4)
e = ar.count(5)
li=[a,b,c,d,e]
print(1+li.index(max(li)))