# beakjoon_2775.py
# 부녀회장이 될테야

t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    fl = [i for i in range(1, n+1)] #0층 숫자 배열

    for _ in range(k):
        for __ in range(1,n):
            fl[__] += fl[__-1]
            #[1,2,3,4]
            #[1,3,3,4]
            #[1,3,6,4]
            #[1,3,6,10]    
    print(fl[-1])



    
            