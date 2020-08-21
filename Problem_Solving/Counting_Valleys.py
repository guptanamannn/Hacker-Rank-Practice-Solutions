import math
import os
import random
import re
import sys


def countingValleys(n, s):
    slide=0
    v=0
    for j,i in enumerate(s):
        if i=="U":
            slide=slide+1
        elif i=="D":
            slide=slide-1
        if slide==0 and i=="U" and j!=0:
            v=v+1
    print(v)



if __name__ == '__main__':
    n = int(input())
    s = input()
    result = countingValleys(n, s)
