# baekjoon_2231.py
# 분해합_셀프넘버 반대? 개념

N = int(input())  # N은 분해합

for i in range(1, N+1):
    cre = i  # 이때의 i(cre)는 생성자
    for j in str(i):  # 생성자를 문자열 함수를 이용해 각자리수로 나눠 더함
        i += int(j)  # 그럼 이때의 i는 각자리수가 더해진 분해합
    if i == N:  # 처음으로 분해합이 입력값과 같을 때의 cre가 가장 작은 생성자
        print(cre)
        break  # 반복문 끝내기
    elif cre == N:  # i(cre)와 입력값이 같다? 그럼 입력값은 생성자가 없다
        print(0)

# 다른 분들 풀이 중 map을 사용하는 것이 눈에 띄임
# 결국 같은 for 문이랑 결과는 같음, 하지만 시간 차이 발생
# 상기 = 시간 1824ms / 하기 = 시간 1560ms

#    N = int(input()) #N은 분해합
#    for i in range(1, N+1):
#        a = sum(list(map(int,str(i)))) # i의 각자리수의 합
#        b = i + a # i에 각자리수의 합 더하면 분해합
#        if b == N:
#            print(i)
#            break
#        elif i == N:
#            print(0)
