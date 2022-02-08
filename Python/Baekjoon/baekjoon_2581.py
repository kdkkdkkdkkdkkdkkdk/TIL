# baekjoon_2581.py
# 소수

M = int(input())
N = int(input())
arry = []

for i in range(M, N+1):
    cnt = 0
    if i == 0:
        pass
    for j in range(2, i+1):
        if i % j == 0:
            cnt += 1
            if cnt > 2:
                break
    if cnt == 1:
        arry.append(i)

if len(arry) != 0:
    print(sum(arry))
    print(min(arry))
else:
    print(-1)

# if cnt > 2:
#    break
# 상기 구문 추가 시 : 30864KB, 1872ms

# for i in range(M, N+1):
#    cnt = 0
#    if i == 0:
#        pass
#    for j in range(2, i+1):
#        if i % j == 0:
#            cnt += 1
#    if cnt == 1:
#        arry.append(i)

# import sys 전 : 30864KB, 4604ms
# import sys 후 : 30864KB, 4712ms or 시간 초과
