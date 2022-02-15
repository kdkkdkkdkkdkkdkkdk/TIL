# baekjoon_3009.py
# 네 번째 점

from pyexpat.errors import XML_ERROR_BINARY_ENTITY_REF


x_arry = []
y_arry = []

for i in range(3):
    x, y = map(int, input().split())
    x_arry.append(x)
    y_arry.append(y)

for i in range(3):
    if x_arry.count(x_arry[i]) == 1:
        a = x_arry[i]
    if y_arry.count(y_arry[i]) == 1:
        b = y_arry[i]

print(a, b)
