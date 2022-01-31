# baekjoon_1427.py
# 소트인사이드
# 내림차순

n = int(input()) 
list = []
for i in str(n):
    list.append(int(i))
list.sort(reverse=True)

for i in list:
    print(i, end = "")

# 한줄 코드
# print(''.join(sorted(input(), reverse=True)))
# '구분자'.join(리스트) : 리스트의 값과 값 사이에 '구분자'에 들어온 구분자를 넣어서 하나의 문자열로 합쳐줌
# sorted(input()) : 리스트 + 오름차순 정렬 한번에