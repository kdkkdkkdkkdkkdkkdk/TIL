# D2

T = int(input())

for test_case in range(1, T+1):

    rows = 10
    cols = 10
    arry = [[0 for j in range(cols)] for i in range(rows)]

    N = int(input())
    for i in range(N):
        a, b, c, d, e = map(int, input().split())
        for j in range(a, c+1):
            for k in range(b, d+1):
                arry[j][k] += e

    cnt = 0
    for i in range(rows):
        for j in range(cols):
            if arry[i][j] == 3:
                cnt += 1
    print('#{} {}'.format(test_case, cnt))
