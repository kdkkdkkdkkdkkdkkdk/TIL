# baekjoon_2798.py
# 블랙잭_브루트 포스

N, M = map(int, input().split())
nums = list(map(int, input().split()))
final_pick = 0
for i in range(0, len(nums)-2):
    for j in range(i+1, len(nums)-1):
        for k in range(j+1, len(nums)):
            current_pick = nums[i]+nums[j]+nums[k]
            if final_pick < current_pick <= M:
                final_pick = current_pick
print(final_pick)
