# baekjoon_1712.py
# 손익분기점

A, B, C = map(int, input().split())
if B >= C:
    print('-1')
else:
    print(int(A/(C-B))+1)
    
# int는 입력한 실수(또는 정수)로부터 얻어진 정수 객체를 반환
# 1.5 -> 1, 1.2 -> 1
