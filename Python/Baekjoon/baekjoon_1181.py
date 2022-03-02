# baekjoon_1181.py
# 단어 정렬

import sys

num = int(sys.stdin.readline())
arry = []
arry_len = []

for i in range(num):
    arry.append(sys.stdin.readline().strip())

arry = list(set(arry))  # 중복 삭제
arry.sort()
arry.sort(key=len)  # 길이 순으로 정렬

for i in arry:
    print(i)

# sys.stdin.readline -- 104ms
# input -- 852ms
