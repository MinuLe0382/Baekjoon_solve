import sys
input = sys.stdin.readline
from collections import deque

dc = [1, -1, 0, 0]
dr = [0, 0, 1, -1]

field = []
n, m = map(int, input().rstrip().split())
matrix = [[0] * (m + 2) for _ in range(n + 2)]
for i in range(1, n + 1):
    matrix[i][1:m + 1] = map(int, input().rstrip()) # 이것도 되고 list(map(int, input().rstrip())) 도 가능하다

# 거리니까 BFS 를 사용해야겠다.

queue = deque([[1, 1]])
while queue:
    r, c = queue.popleft()
    cur = matrix[r][c]
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if matrix[nr][nc] == 1:
            queue.append([nr, nc])
            matrix[nr][nc] = cur + 1

print(matrix[n][m])