# baekjoon_10250.py
# ACM 호텔

num = int(input())
for i in range(num):
    H, W, N = map(int, input().split())
    R_N = 1
    while N > H:
        N -= H
        R_N += 1
    print(N*100+R_N)
