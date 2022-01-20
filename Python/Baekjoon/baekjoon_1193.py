# baekjoon_1193.py
# 분수찾기

# 규칙성을 찾는 것이 포인트

num = int(input()) # num = 7
line = 1
while num > line: # while 문 탈출하면 'line'번째 줄의 'num'번째 위치
    num -= line   # num = 1, line = 4
    line += 1


if line % 2 == 0:  # 짝수번째 줄
    numerator = num
    denominator = line - num + 1
else:
    numerator = line - num + 1
    denominator = num

print(numerator, "/", denominator, sep="") #sep default는 space, "" 선언으로 붙여줌
