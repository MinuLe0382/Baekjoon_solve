import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

matrix = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    matrix[i][1:] = list(map(int, input().rstrip().split()))

# 누적합 구하기
for i in range(1, n + 1):
    for j in range(1, n + 1):
        matrix[i][j] += matrix[i - 1][j] + matrix[i][j - 1] - matrix[i - 1][j - 1]
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = matrix[x2][y2] - matrix[x1 - 1][y2] - matrix[x2][y1 - 1] + matrix[x1 - 1][y1 - 1]
    print(result)