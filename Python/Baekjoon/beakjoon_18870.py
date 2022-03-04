# baekjoon_18870.py
# 좌표 압축

# 몇번째 순서인지로 좌표를 부여

import sys

input = sys.stdin.readline

num = int(input())
arry = list(map(int, input().split()))
arry2 = sorted(set(arry))

dic = {}
for i in range(len(arry2)):
    dic[arry2[i]] = i

for _ in arry:
    print(dic[_], end=' ')
