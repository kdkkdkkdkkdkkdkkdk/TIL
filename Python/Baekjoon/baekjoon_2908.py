# baekjoon_2908.py
# 상수

a, b = input().split()

new_a = int(a[::-1])
new_b = int(b[::-1])

if new_a > new_b:
    print(new_a)

elif new_a < new_b:
    print(new_b)
    
#*정수형은 reverse 함수를 사용할 수 없다. reverse 함수는 list 자료형에만 사용할 수 있다.
#*숫자를 문자열로 입력받고, 슬라이싱을 이용해 뒤집어주었다.
#*★[::-1]
