# baekjoon_2108.py
# 통계학

import sys
from collections import Counter #최빈값을 위함
input = sys.stdin.readline

n = int(input())
arry = []

for i in range(n):
    arry.append(int(input()))

#산술평균
print(round(sum(arry)/n))

#중앙값
st_ary = sorted(arry)
len_st_ary = len(st_ary)
if n % 2 == 1:
    print(st_ary[int((len_st_ary-1)/2)])
else:
    print(int(st_ary[int((len_st_ary-1)/2)]+st_ary[int((len_st_ary-1)/2)+1])/2)

#최빈값

cnt_arry = Counter(st_ary).most_common()
#정렬된 arry를 사용해야 두번째로 작은 값을 출력할 수 있음
#[(-2, 1), (1, 1), (2, 1), (3, 1), (8, 1)]
if len(cnt_arry) > 1 and cnt_arry[0][1] == cnt_arry[1][1]:
    print(cnt_arry[1][0])
else:
    print(cnt_arry[0][0])
    

#범위    
print(abs(max(arry)-min(arry)))