# baekjoon_11729.py
# 하노이탑 이동순서 - 재귀함수 사용
# 재귀함수 문제의 대표적인 유형

def hanoi(n, a, c, b):  # a : 시작, b : 보조, c : 목표
    if n == 1:
        print(a, c)  # 원반 1개 -> 원반을 목표 기둥으로 이동
        return
    else:
        hanoi(n-1, a, b, c)  # 제일 큰 원반 제외, 나머지 원반들을 모두 보조 기둥으로 이동
        print(a, c)  # 제일 큰 원반을 목표 기둥으로 이동
        hanoi(n-1, b, c, a)  # 보조 기둥에 있는 나머지 원반들을 목표 기둥으로 이동


x = int(input())
print(2**x-1)
hanoi(x, 1, 3, 2)

# hanoi(3,1,3,2)
# hanoi(2,1,2,3)
# hanoi(1,1,3,2)
#print(1,3) -----1
#print(1,2) ---------2
# hanoi(1,3,2,1)
#print(3,2) -----3
#print(1,3) -------------4
# hanoi(2,2,3,1)
# hanoi(1,2,1,3)
#print(2,1) -----5
#print(2,3) ---------6
# hanoi(1,1,3,2)
#print(1,3) -----7
