# baekjoon_1316.py
# 그룹 단어 체커

num = int(input())
group_cnt = num
for i in range(0, num):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        # word[j] != word[j+1] 이라면, 남은 문자 중에 word[j]와 같은 문자가 있는지 확인하여, 존재한다면 그룹 단어가 아니다.
        elif word[j] in word[j+1:]:
            group_cnt -= 1
            break

print(group_cnt)

# break 를 추가함으로써 연산 속도를 올릴 수 있다.
# range(0, 5) -> for 문의 결과값으로 0, 1, 2, 3, 4
# range(0, len(word)-1) -> 마지막 문자열 확인은 len(word)-1에서 j+1로
