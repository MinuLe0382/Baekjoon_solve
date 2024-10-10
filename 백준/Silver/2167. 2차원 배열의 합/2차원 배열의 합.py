import sys
input = sys.stdin.readline

alist = []

n, m = map(int, input().rstrip().split())
matrix = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    matrix[i][1:] = list(map(int, input().rstrip().split()))

for r in range(1, n + 1):
    for c in range(1, m + 1):
        matrix[r][c] += matrix[r - 1][c] + matrix[r][c - 1] - matrix[r - 1][c - 1]

k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(matrix[x][y] - matrix[x][j - 1] - matrix[i - 1][y] + matrix[i - 1][j - 1])