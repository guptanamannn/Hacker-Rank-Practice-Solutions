# -*- coding: utf-8 -*-
"""
Created on Sun May  6 18:10:54 2018

@author: dms24081999
"""

time=input()
if time[-2:]=='AM':
    sept=time[:-2].split(':')
    if int(sept[0])==12:
        nhour='00'
    else:
        nhour=str(sept[0])
elif time[-2:]=='PM':
    sept=time[:-2].split(':')
    if int(sept[0])==12:
        nhour='12'
    else:
        nhour=int(sept[0])+12

nt=[]
nt.append(str(nhour))
nt.append(str(sept[1]))
nt.append(str(sept[2]))
new_time=":".join(nt)
print(new_time)