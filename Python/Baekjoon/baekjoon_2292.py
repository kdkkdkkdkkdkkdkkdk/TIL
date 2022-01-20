# baekjoon_2292.py
# 벌집

num = int(input())

cnt = 1
room = 1
cnt_multiple = 6

while num > cnt:
    room += 1
    cnt += cnt_multiple
    cnt_multiple += 6

print(room)

# 규칙 잘 찾기
# 1 / 2 ~ 7 / 8 ~ 19 / 20 ~ 37 / ...
# 1개 / 6개 / 18개 / 24개 / ...
# 1개 / 2개 / 3개 / 4개 / ...
