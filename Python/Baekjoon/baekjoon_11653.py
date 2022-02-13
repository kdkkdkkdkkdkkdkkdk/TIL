# baekjoon_11653.py
# 소인수분해

num = int(input())
i = 2
while num > 1:
    if num % i == 0:
        num = num // i
        print(i)
    else:
        i += 1

# 시간 줄여보기
# import sys + while num > 1: -- 30864KB / 1480ms
# import sys + while num >= i: -- 30864KB / 1628ms
# while num > 1: -- 30864KB / 1440ms
# while num >= i: -- 30864KB / 1808ms
