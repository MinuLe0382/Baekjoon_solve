from collections import deque

dc = [-1, 1, -2, 2, -1, 1]
dr = [-2, -2, 0, 0, 2 , 2]
n = int(input())
r1, c1, r2, c2 = map(int, input().split())
flag = False
matrix = [[0] * n for _ in range(n)]
queue = deque([[r1, c1]])
matrix[r1][c1] = 1

while queue:
    r, c = queue.popleft()
    cur = matrix[r][c]
    for d in range(6):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < n and 0 <= nc < n:
            if matrix[nr][nc] == 0:
                queue.append([nr, nc])
                matrix[nr][nc] = cur + 1
            elif nr == r2 and nc == c2:
                flag = True
                queue = deque([])
                break
if flag == False:
    print(-1)
else:
    print(matrix[r2][c2] - 1)