# baekjoon_1002.py
# 터렛

# 원과 원의 접점의 개수를 구하는 문제
# 원과 원의 위치 관계를 알고 있어야 풀 수 있는 문제
# 만나지 않는 경우 - 0개/ 접하는 경우 - 1개/ 두 점에서 만나는 경우 - 2개/ 두 원이 겹치는 경우 - 무한개

num = int(input())

for i in range(num):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))
    dis = ((x2-x1)**2+(y2-y1)**2)**(1/2)

    if dis == 0:
        if r1 == r2:
            print(-1)  # 두 원이 겹치는 경우
        else:
            print(0)  # 동심원인 경우 - 만나지 않음
    else:
        if dis == r1+r2 or dis == abs(r1-r2):
            print(1)  # 접하는 경우
        elif (dis > abs(r1-r2)) and (dis < r1+r2):
            print(2)  # 두 점에서 만나는 경우
        else:
            print(0)  # 외부, 내부에서 만나지 않음
