import math
import os
import random
import re
import sys
import string

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    d=dict()
    for i,x in enumerate(string.ascii_lowercase[:26]):
        d[x]=h[i]
    lst=list()
    for x in word:
        lst.append(d[x])
    print(max(lst)*len(word))



if __name__ == '__main__':
    h = list(map(int, input().rstrip().split()))
    word = input()
    result = designerPdfViewer(h, word)

