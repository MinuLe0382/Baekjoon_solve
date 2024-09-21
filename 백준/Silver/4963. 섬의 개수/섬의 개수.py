import sys
input = sys.stdin.readline
from collections import deque

# 8방향
dc = [1, -1, 0, 0, 1, -1, 1, -1]
dr = [0, 0, 1, -1, 1, 1, -1, -1]

while True:
    w, h = map(int, input().rstrip().split())
    if w == 0 and h == 0:
        break
    matrix = [[0] * (w + 2) for _ in range(h + 2)]
    for i in range(1, h + 1):
        matrix[i][1:w + 1] = list(map(int, input().rstrip().split()))

    number = 0
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if matrix[i][j] == 1: # 1인 구역일때 BFS를 실행, BFS로 안가본 지역에서 여러번 BFS를 실행하게 될 것.
                number += 1
                queue = deque([[i, j]])
                matrix[i][j] = 0 # 방문
                while queue:
                    r, c = queue.popleft()
                    for d in range(8):
                        nr = r + dr[d]
                        nc = c + dc[d]
                        if matrix[nr][nc] == 1:
                            queue.append([nr, nc])
                            matrix[nr][nc] = 0
    print(number)