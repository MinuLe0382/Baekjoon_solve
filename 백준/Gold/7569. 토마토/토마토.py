import sys
input = sys.stdin.readline
from collections import deque

dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# 밭에서 1인 부분을 일단 모두 deque에 넣고 순차적으로 DFS를 돌리면 어떻게든 되지 않을까?
# 밭을 구성한다.
M, N, H = map(int, input().rstrip().split())
matrix = [[[-1] * (M + 2) for _ in range(N + 2)] for k in range(H + 2)]
for z in range(1, H + 1):
    for i in range(1, N + 1):
        matrix[z][i][1:M + 1] = list(map(int, input().rstrip().split()))

# 밭에서 1인 칸을 찾아 QUEUE에 집어넣는다.
queue = deque([])
#print(matrix)
for z in range(1, H + 1):
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if matrix[z][j][i] == 1:
                queue.append([z, j, i])

# DFS
while queue:
    z, r, c = queue.popleft()
    cur = matrix[z][r][c]
    for d in range(6):
        nr = r + dr[d]
        nc = c + dc[d]
        nz = z + dz[d]
        if matrix[nz][nr][nc] == 0:
            queue.append([nz, nr, nc])
            matrix[nz][nr][nc] = cur + 1 # 익는 날짜 + 1임

# 0인 부분이 있으면 -1
flag = True
maximum = 0
for z in range(1, H + 1):
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            num = matrix[z][j][i]
            if num == 0:
                flag = False
                print(-1)
                break
            else:
                maximum = max(maximum, num)
        if flag == False:
            break
        
if flag == True:
    print(maximum - 1)