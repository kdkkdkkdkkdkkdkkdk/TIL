# baekjoon_11651.py
# 좌표 정렬하기 2

import sys
n = int(input())
number = []

for i in range(n):
    x,y = map(int, sys.stdin.readline().split())
    number.append((y,x))

number = sorted(number)

for i in range(n):
    print(number[i][1],number[i][0])
    
#다른 출력 방법
#for y, x in number:
#   print(x, y)