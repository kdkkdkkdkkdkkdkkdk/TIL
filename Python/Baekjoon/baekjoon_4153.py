# baekjoon_4153.py
# 직각삼각형

while True:
    x, y, z = map(int, input().split())
    if x == 0 and y == 0 and z == 0:
        break

    if x**2 + y**2 == z**2:
        print('right')
    elif y**2 + z**2 == x**2:
        print('right')
    elif z**2 + x**2 == y**2:
        print('right')
    else:
        print('wrong')
