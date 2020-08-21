import math
import os
import random
import re
import sys


def formingMagicSquare(s):
    length=len(s)
    olength=int(length*(length**2+1)/2)
    minimum=0
    for i,r1 in enumerate(s):
        if sum(r1)!=olength:
            for j,r2 in enumerate(r1):
                if s[i][j]%2!=0 and i%2==0 and j%2==0:
                    # print(olength-(sum(r1)-s[i][j]),s[i][j])
                    minimum=minimum+abs((olength-(sum(r1)-s[i][j]))-s[i][j])
                    # print(minimum)
                    break
                elif s[i][j]%2==0 and (i%2!=0 or j%2!=0):
                    # print(olength-(sum(r1)-s[i][j]),s[i][j])
                    minimum=minimum+abs((olength-(sum(r1)-s[i][j]))-s[i][j])
                    # print(minimum)
                    break
                elif s[i][j]%2==0 and i%2==0 and j%2==0 and len(list(set(r1)))<length:
                    # print(olength-(sum(list(set(r1)))),s[i][j])
                    minimum=minimum+abs((olength-(sum(list(set(r1)))))-s[i][j])
                    # print(minimum)
                    break
    print(minimum)
                
        



if __name__ == '__main__':
    s = []
    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))
    result = formingMagicSquare(s)