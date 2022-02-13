# baekjoon_11653.py
# 소인수분해

import sys
input = sys.stdin.readline

num = int(input())
i = 2
while num >= i:
    if num % i == 0:
        num = num // i
        print(i)
    else:
        i += 1
