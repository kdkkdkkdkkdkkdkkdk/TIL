# baekjoon_1011.py
# Fly me to the Alpha Contauri

import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    x,y = map(int,input().split())
    dist = y-x # 이동 거리
    cnt = 0 # 동작 횟수
    move = 1 # 1회 움직이는 거리(이동폭)
    total_move = 0 # 이동 거리의 합
    
    while total_move < dist:
        cnt += 1
        total_move += move
        if cnt % 2 == 0: # 규칙에 따라 2번 이동 후 이동폭을 +1 
                         # ex) 1,1/2,2/3,3/...
            move += 1
    print(cnt)

#단, 이렇게 하면 3이 입력되었을 때 total_move와 실제 계산값과 다름

    
