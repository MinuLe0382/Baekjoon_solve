from heapq import heappop, heappush
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
tc = 0
while True:
    N = int(input())
    if N == 0:
        break
    tc += 1
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
    
    heap = [(matrix[0][0], (0, 0))]
    dist = [[float('INF')] * N for _ in range(N)]
    while heap:
        # 방문 (누적 가중치, cur)
        wei, cur = heappop(heap)
        if dist[cur[0]][cur[1]] != float('INF'): # 이미 갱신이 되어있다. (최초방문이 최단거리)
            continue

        dist[cur[0]][cur[1]] = wei
        # 탐색
        for d in range(4):
            nr = cur[0] + dr[d]
            nc = cur[1] + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if dist[nr][nc] == float('INF'):
                    heappush(heap, (wei + matrix[nr][nc], (nr, nc))) # 프림과의 결정적인 차이
    print(f"Problem {tc}: {dist[N - 1][N - 1]}")