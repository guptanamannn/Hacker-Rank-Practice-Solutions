# -*- coding: utf-8 -*-
"""
Created on Fri May  4 18:04:56 2018

@author: dms24081999
"""

letter_s={}
mod_s=[]
s=input()

for ch in s:
    i=0
    for rep in s:
        if rep == ch:
            i=i+1
#    print(ch+"="+str(i))
    letter_s.setdefault(ch,i)
#    print(letter_s)
for keys,value in letter_s.items():
    if value%2!=0:
        mod_s.append(keys)
#        print(mod_s)
mod_s.sort()
for ch in s:
    ch==mod_s
s="".join(mod_s)
if not s:
    print("Empty String")
else:
    print(s)