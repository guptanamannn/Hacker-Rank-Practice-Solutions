import math
import os
import random
import re
import sys


def climbingLeaderboard(scores, alice):
    score=sorted(list(set(scores)),reverse=True)
    for i,x in enumerate(alice):
        try:
            result = list(filter(lambda i: i <= x, score))[0]
            res=score.index(result)+1
        except:
            res=len(score)+1
        print(res)
        

if __name__ == '__main__':
    scores_count = int(input())
    scores = list(map(int, input().rstrip().split()))
    alice_count = int(input())
    alice = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard(scores, alice)









# Complete the climbingLeaderboard function below.
# def climbingLeaderboard(scores, alice):
#     score=sorted(list(set(scores)),reverse=True)
#     for i,x in enumerate(alice):
#         res = [idx+1 for idx, val in enumerate(score) if val <= x] 
#         if len(res)==0:
#             res.append(len(score)+1)
#         print(min(res))