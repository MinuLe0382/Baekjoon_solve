N, K = map(int, input().split())
bmp = [input().split() for _ in range(N)]

for row in bmp:
    # 가로 방향 확대
    expanded_row = [pixel * K for pixel in row]
    expanded_row = list(''.join(expanded_row))

    # 세로 방향 확대
    for _ in range(K):
        print(*expanded_row)