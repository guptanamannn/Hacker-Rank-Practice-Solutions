# -*- coding: utf-8 -*-
"""
Created on Sat May  5 21:55:56 2018

@author: dms24081999
"""

import string
s=input()
count=1
for ch in s:
    if ch in string.ascii_uppercase:
        count=count+1
print(count)