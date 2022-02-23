# baekjoon_3053.py
# 택시 기하학

import math

x1 = 0
y1 = 0

x2 = int(input())
y2 = x2

print(math.pi*(abs(x1-x2)**2))
print(2*(abs(x1-x2)*abs(y1-y2)))
