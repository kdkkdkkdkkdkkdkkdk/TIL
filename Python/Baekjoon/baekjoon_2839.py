# baekjoon_2839.py
# 설탕 배달

#five + three의 최솟값 -> 가능한 five가 많도록
#'N'kg의 설탕, 5kg 설탕 주머니로 나눠지지 않으면 3kg 설탕 주머니를 하나씩 채워주며 N-=3

N = int(input())

five = 0
three = 0

while N >= 0: # N=0의 경우를 놓치면 3의 배수 중 -1이 출력되는 수(3,6,9,12)가 생김
    if N % 5 == 0:
        five += N // 5
        print(five+three)
        break
    N -= 3
    three += 1
else:
    print(-1)
