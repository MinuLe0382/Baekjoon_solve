N, T, C, P = map(int, input().split())

# 한 칸(플롯)이 얻을 수 있는 수확 횟수 = (N-1)//T
# 전체 수확 개수 = 수확 횟수 × C
# 수익 = 전체 수확 개수 × P
print(((N - 1) // T) * C * P)