from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    field = [[1] * (n + 2) for _ in range(n + 2)]
    for k in range(1, n + 1):
        field[k][1:n+1] = list(map(int, input().rstrip()))
    flag = True
  
    # 출발점 찾기
    for i in range(1, n + 2):
        for j in range(1, n + 2):
            if field[i][j] == 2:
                flag = False
                break
        if flag == False:
            break
    queue = deque([])
    queue.append([i, j, 0]) # 거리또한 포함해서 QUEUE에 넣는다.
  
   # BFS 실행
    while queue:
        y, x, cur_dist = queue.popleft()
        for d in range(4): # 탐색
            nx = x + dx[d]
            ny = y + dy[d]
            if field[ny][nx] == 0:
                field[ny][nx] = 1
                queue.append([ny, nx, cur_dist + 1])
            elif field[ny][nx] == 3:
                print(f'#{tc} {cur_dist}')
                break
        else:
            continue
        break
    else:
        print(f'#{tc} {0}')
