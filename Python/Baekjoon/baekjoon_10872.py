# baekjoon_10872.py
# 팩토리얼 - 재귀함수

# 재귀함수 - 자기 자신을 다시 호출하는 함수

def factorial(n):
    if n <= 1:
        return 1  # 0! = 1, 1! = 1
    return n * factorial(n-1)


a = int(input())
print(factorial(a))

# 5*factorial(4)
# 5*4*factorial(3)
# 5*4*3factorial(2)
# ...

# for문 사용

# def factorial(n):
#   result = 1
#   for i in range(1,n+1): #1부터 n까지 곱하려고함
#       result *= i
#   return result
