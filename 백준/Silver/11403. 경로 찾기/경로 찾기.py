from collections import deque

# 입력 처리
n = int(input())  # 정점의 개수
graph = [list(map(int, input().split())) for _ in range(n)]

# 결과를 저장할 행렬
result = [[0] * n for _ in range(n)]

# 각 정점에서 BFS 수행
for i in range(n):
    queue = deque([i])
    visited = [False] * n

    while queue:
        v = queue.popleft()
        
        for j in range(n):
            if graph[v][j] == 1 and not visited[j]:
                visited[j] = True
                result[i][j] = 1
                queue.append(j)

# 결과 출력
for row in result:
    print(" ".join(map(str, row)))