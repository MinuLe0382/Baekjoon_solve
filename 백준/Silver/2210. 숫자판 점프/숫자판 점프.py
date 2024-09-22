board = [list(map(int, input().split())) for _ in range(5)]

# 중복을 피하기 위해 set 사용
result_set = set()

# 상하좌우 이동을 위한 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# DFS 함수 정의
def dfs(x, y, number):
    # 6자리 숫자가 되면 결과에 추가
    if len(number) == 6:
        result_set.add(number)
        return
    
    # 상하좌우로 이동하며 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 좌표가 유효한 범위 내에 있을 때만 이동
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, number + str(board[nx][ny]))

# 모든 좌표에서 DFS 탐색 시작
for i in range(5):
    for j in range(5):
        dfs(i, j, str(board[i][j]))

# 결과 출력
print(len(result_set))