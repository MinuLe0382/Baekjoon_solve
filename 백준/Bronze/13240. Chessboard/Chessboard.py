N, M = map(int, input().split())

# 출력
for i in range(N):
    for j in range(M):
        if (i+j) % 2 == 0:
            print('*', end='')
        else:
            print('.', end='')
    print()