import math
import os
import random
import re
import sys

def catAndMouse(x, y, z):
    if abs(x-z)==abs(y-z):
        print("Mouse C")
    elif abs(x-z)<abs(y-z):
        print("Cat A")
    elif abs(x-z)>abs(y-z):
        print("Cat B")

if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        xyz = input().split()
        x = int(xyz[0])
        y = int(xyz[1])
        z = int(xyz[2])
        result = catAndMouse(x, y, z)
