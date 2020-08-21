# -*- coding: utf-8 -*-
"""
Created on Sun May  6 14:27:47 2018

@author: dms24081999
"""

n=int(input())
a=[]
sum1=0
sum2=0
for i in range(0,n):
    a.append(list(map(int, input().split())))

for i in range(0,n):
    sum1=sum1+a[i][i]
    
for i in range(0,n):
    sum2=sum2+a[i][n-i-1]

total=sum1-sum2

print(abs(total))