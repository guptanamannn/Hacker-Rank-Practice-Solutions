import math
import os
import random
import re
import sys

def hurdleRace(k, height):
    if max(height)>k:
        print(max(height)-k)
    else:
        print(0)
    


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    height = list(map(int, input().rstrip().split()))
    result = hurdleRace(k, height)
