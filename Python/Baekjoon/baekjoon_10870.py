# baekjoon_10870.py
# 피보나치 - 재귀함수 사용

def pibonacci(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return pibonacci(n-1)+pibonacci(n-2)


a = int(input())
print(pibonacci(a))
