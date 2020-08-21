# -*- coding: utf-8 -*-
"""
Created on Sun May  6 15:36:25 2018

@author: dms24081999
"""

n=int(input())
sd=n-1
for i in range(n):
    print(str(" "*(sd-i))+str("#"*(i+1)))
