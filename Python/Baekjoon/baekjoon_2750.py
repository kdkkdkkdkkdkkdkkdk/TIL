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
    
# 버블 정렬 : 현재 배열 요소와 그 다음 배열 요소를 비교한다음 조건에 걸리면 교환
# for i in range(len(number)):
#   for j in range(len(number)):
#       if number[i] < number[j]:
#           number[i],number[j] = number[j],number[i]

# 삽입 정렬 : 배열의 한 원소인 key 값을 우선 가지고 있으며, 이 key를 알맞은 자리에 삽입
# for i in range(1, len(number)):
#   while (i>0) & (number[i]<number[i-1]):
#       number[i],number[i-1] = number[i-1],number[i]
#       i-=1