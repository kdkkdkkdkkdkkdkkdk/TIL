# beakjoon_1085.py
# 직사각형에서 탈출

x, y, w, h = map(int, input().split())
print(min(x, y, w-x, h-y))

# x, y, w, h = map(int, input().split()) -- 72ms
# x, y, w, h = list(map(int, input().split())) -- 68ms
