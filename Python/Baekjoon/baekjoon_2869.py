# baekjoon_2869.py
# 달팽이는 올라가고 싶다

A, B, V = map(int, input().split())

day = (V-B)/(A-B)  # 며칠 소요되는지 바로 확인, 정수로 떨어지면 정수만큼, 분수로 떨어지면 내림,정수화 후 +1일

if day == int(day):  # 내림, 정수화, 정수인지 확인
    day = int(day)
else:  # 나머지 경우는 분수(소수)
    day = int(day)+1

print(day)

#A, B, V = map(int,input().split())
#x = 0
#cnt = 0
# while (A-B)*x < V:
#    x+=1

# >> while 문으로 하루하루 계산하려니 너무 오래 걸리는 것을 확인
# >>

# if (A-B)*x == V:
#    cnt = x-1
# else:
#    cnt = x
# print(cnt)
