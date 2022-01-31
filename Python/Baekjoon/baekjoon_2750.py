# baekjoon_2750.py
# 수 정렬하기_정렬
# 시간 복잡도가 O(n**2)인 정렬 알고리즘
# ex) 삽입 정렬, 거품 정렬 등

n = int(input())
number = []

for i in range(n):
    num = int(input())
    number.append(num)
    
sorted_number = sorted(number)

for i in range(n):
    print(sorted_number[i])