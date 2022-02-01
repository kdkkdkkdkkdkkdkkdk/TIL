# baekjoon_11650.py
# 좌표 정렬하기
import sys
n = int(input())
number = []

for i in range(n):
    num = list(map(int, sys.stdin.readline().split())) #이렇게 변수 하나로 두 입력값을 넣는 것 보다 변수 두개 선언하고 두 입력값을 넣는 것이 메모리, 시간 측면에서 나음
    number.append(num) #여기서도 다른 것보다 튜플이 가장 메모리, 시간 측면에서 나음

number = sorted(number)

for i in range(n):
    print(number[i][0],number[i][1])


#input()을 이용할 때 종종 시간 초과가 발생하기 때문에 sys모듈의 sys.stdin을 사용.
#시간이 너무 길어져서 써보기로 함

#input() 메모리 51248KB, 4604ms
#sys.stdin.readline() 메모리 51248KB, 540ms

#for i in range(n):
#   a,b = map(int, sys.stdin.readline().split())
#   number.append((a,b))
#튜플로 바꾸면 메모리 45104KB, 392ms
#리스트로 바꾸면 메모리 46128KB, 408ms