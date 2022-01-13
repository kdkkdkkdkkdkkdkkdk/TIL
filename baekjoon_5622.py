# baekjoon_5622.py
# 다이얼

alp = input()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
num = 0

for y in alp:
    for i in dial:
        for x in i:
            if y == x:
                num += dial.index(i)+3

print(num)

#코드 한줄 줄이기↓

#for y in alp:
#  for i in dial:
#    if y in i
#      num += dial.index(i)+3

#백준 제출 결과, 동일함.
#메모리 : 30860 KB, 시간 : 68 ms
#코드 길이만 214 B VS. 187 B
