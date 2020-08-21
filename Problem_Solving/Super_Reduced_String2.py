# -*- coding: utf-8 -*-
"""
Created on Sat May  5 22:16:27 2018

@author: dms24081999
"""

mod_s = []
reduced = []
s = input()

for ch in s:
    i = 0
    for rep in s:
        if rep == ch:
            i = i+1
    if i % 2 != 0:
        mod_s.append(ch)
for ch in mod_s:
    if ch not in reduced:
        reduced.append(ch)
s = "".join(reduced)
if not s:
    print("Empty String")
else:
    print(s)
