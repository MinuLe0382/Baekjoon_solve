# 입력
n = int(input())

# 합 구하기
sum1 = n*(n+1)//2  # 1부터 n까지의 합
sum2 = (n+1)*(n+2)//2-1  # 2부터 n+1까지의 합

# 짝수 판별
res1 = sum1 % 2
res2 = sum2 % 2

# 출력
if res1 == res2 == 0:
    print(2)
elif res1 == res2 == 1:
    print(1)
else:
    print(0)