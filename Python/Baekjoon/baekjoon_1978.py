# baekjoon_1978.py
# 소수찾기

iter = int(input())
nums = list(map(int, input().split()))
prime = 0

for i in nums:
    cnt = 0  # 매번 0으로 초기화되야함
    if i == 1:  # i == 1 일 때 넘기기
        pass
    for j in range(2, i+1):  # 2부터 i까지 나누기
        if i % j == 0:  # 나머지가 0이면 cnt + 1
            cnt += 1
    if cnt == 1:  # 소수라면 나머지가 0인 경우가 본인이 본인을 나눴을 때 뿐
        prime += 1

print(prime)

# 루트 **(1/2)
# pass : 실행할 코드가 없는 것으로 다음 행동을 계속해서 진행함
# continue : 바로 다음 순번의 loop를 수행
# break : 반복문을 멈추고 loop 
