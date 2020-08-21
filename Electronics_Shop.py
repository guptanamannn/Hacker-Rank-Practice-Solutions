import os
import sys

def getMoneySpent(keyboards, drives, b):
    lst=list()
    for i in range(len(keyboards)):       
        for j in range(len(drives)):
            if keyboards[i]+drives[j]<=b:
                lst.append(keyboards[i]+drives[j])
    if len(lst)!=0:
        print(max(lst))
    else:
        print(-1)


if __name__ == '__main__':
    bnm = input().split()
    b = int(bnm[0])
    n = int(bnm[1])
    m = int(bnm[2])
    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))
    moneySpent = getMoneySpent(keyboards, drives, b)
