N, M = map(int, input().split())

edges = []
for _ in range(M):
    s, e, w = map(int, input().split())
    edges.append((s, e, w))
    
dist = [float('INF')] * (N + 1)
dist[1] = 0

for _ in range(N):
    updated = False
    for cur, nxt, w in edges:
        if dist[cur] == float('INF'): # 사용불가한 간선
            continue
        if dist[nxt] > dist[cur] + w:
            dist[nxt] = dist[cur] + w # 업데이트
            updated = True
    if updated == False: # 이게 최선의 배열이라는 의미
        break
# 위 for문의 결과는 다익스트라의 결과와 완전히 동일하다.
if updated == True:
    print(-1)
else:
    for i in range(2, N + 1):
        if dist[i] == float('INF'):
            print(-1)
        else:
            print(dist[i])