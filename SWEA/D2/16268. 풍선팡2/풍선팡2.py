dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
testcase = int(input())

for tc in range(testcase):
    M, N = map(int, input().split())
    mat = [[0] * (N + 2) for _ in range(M + 2)]
    matrix = [list(map(int, input().split())) for _ in range(M)]
    for i in range(1, M + 1):
        mat[i][1:N + 1] = matrix[i - 1]
    maximum = 0
    for r in range(1, M + 1):
        for c in range(1, N + 1):
            summation = mat[r][c]
            for d in range(4):
                nc, nr = c + dc[d], r + dr[d]
                summation += mat[nr][nc]
            if summation > maximum:
                maximum = summation
    print(f"#{tc + 1} {maximum}")