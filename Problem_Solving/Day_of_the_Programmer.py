# -*- coding: utf-8 -*-
"""
Created on Tue May  8 17:58:17 2018

@author: dms24081999
"""

year=int(input())
progday=[]
day=13
month='09'
if year>=1700 and year<=2700:
    if year%4==0:
        leap=1
        if year%100!=0:
            leap=1
            if year%400==0:
                leap=1
    else: 
        leap=0
    if leap==1:
        day-=1
    progday.append(str(day))
    progday.append(str(month))
    progday.append(str(year))
    print(".".join(progday))
    
