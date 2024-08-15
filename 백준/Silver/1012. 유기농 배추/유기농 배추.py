import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(T):
    m, n, k = map(int, input().rstrip().split())
    field = [[0] *  (m + 2) for _ in range(n + 2)]
    for i in range(1, k + 1):
        x, y = map(int, input().rstrip().split())
        field[y + 1][x + 1] = 1

    field
    cnt = 0
    for y in range(1, n + 1):
        for x in range(1, m + 1): # 배추가 있는 모든 좌표에서 DFS를 실시
            if field[y][x] == 1: 
                cnt += 1
                stack = [(y, x)]
                field[y][x] = 0 # 주변 4자리 말고 현재 자리도 방문기록
                while stack:
                    cur = stack.pop()
                    for d in range(4):
                        ny, nx = cur[0] + dy[d], cur[1] + dx[d]
                        if field[ny][nx] == 1:
                            stack.append((ny, nx))
                            field[ny][nx] = 0
    print(cnt)