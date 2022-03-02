# baekjoon_10814.py
# 나이순 정렬

# 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬

import sys

input = sys.stdin.readline

num = int(input())
arry = []

for _ in range(num):
    arry.append(list(input().split()))

arry.sort(key=lambda x: int(x[0]))  # 첫 번째 인자 기준 오름차순으로 정렬, 첫 번째 인자 int화 필수

for i in arry:
    print(i[0], i[1])
