import math
import os
import random
import re
import sys


def pickingNumbers(a):
    unique=sorted(list(set(a)))
    alllengths=[0]
    for i,x in enumerate(unique):
        if i+1!=len(unique):
            if abs(unique[i]-unique[i+1])<2:
                alllengths.append(a.count(unique[i])+a.count(unique[i+1]))
        elif(len(unique)==1):
            alllengths.append(a.count(unique[i]))
    print(max(alllengths))



if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = pickingNumbers(a)
