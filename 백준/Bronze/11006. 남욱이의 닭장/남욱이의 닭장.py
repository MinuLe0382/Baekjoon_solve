T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    leg = M * 2 - N
    print(leg, M - leg)