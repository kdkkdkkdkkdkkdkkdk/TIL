# baekjoon_1436.py
# 영화감독 숌_브루트 포스

n = int(input())
number = 666
cnt = 0

while True: # 참일 때까지 반복문
    if '666' in str(number):
        cnt += 1
    if cnt == n: # 2 -> 666, 1666
        print(number)
        break
    number += 1
    