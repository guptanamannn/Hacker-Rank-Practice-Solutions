import os
import sys

def pageCount(n, p):
    start=1
    y,x=0,0
    for i in range(1,p,2):
        y=y+1

    if n%2!=0:
        for j in range(n-1,p,-2):
            x=x+1
    else:
        for j in range(n,p,-2):
            x=x+1
    print(min(y,x))

if __name__ == '__main__':
    n = int(input())
    p = int(input())
    result = pageCount(n, p)