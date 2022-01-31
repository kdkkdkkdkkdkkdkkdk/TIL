# baekjoon_7568.py
# 덩치_브루트 포스

num = int(input())
nums = []
for i in range(num):
    case = list(map(int,input().split()))
    nums.append(case)

for i in nums:
    rank = 1
    for j in nums:
        if i[0] < j[0] and i[1] < j[1]: #키, 몸무게 모두 클 때 등수 +1
            rank +=1
    print(rank, end=" ")
    
#sep="" - print문의 출력문들 사이에 해당하는 내용 넣음, 출력문 사이에 구분자
#end="" - default \n (줄바꿈), 출력문 끝에 구분자