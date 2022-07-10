# D3

T = int(input())

for test_case in range(1, T+1):

    K, N, M = map(int, input().split())
    charge_location = list(map(int, input().split()))
    bus = cnt = 0

    while bus + K < N:
        for can_charge in range(K, 0, -1):
            if (bus + can_charge) in charge_location:
                bus += can_charge
                cnt += 1
                break
        else:
            cnt = 0
            break

    print('#{} {}'.format(test_case, cnt))
