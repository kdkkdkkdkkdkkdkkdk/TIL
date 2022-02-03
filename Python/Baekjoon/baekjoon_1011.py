# baekjoon_1011.py
# Fly me to the Alpha Contauri

import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    x,y = map(int,input().split())
    dist = y-x
    cnt = 0
    move = 1
    total_move = 0
    
    while total_move < dist:
        cnt += 1
        total_move += move
        if cnt % 2 == 0:
            move += 1
    print(cnt)

    
