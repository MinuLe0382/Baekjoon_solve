from collections import deque

N, K = map(int, input().split())
dist = list(-1 for _ in range(0, 100001))

dist[N] = 0

queue = deque([N])
while queue:
    cur = queue.popleft()
    if cur == K:
        break
    if cur * 2 <= 100000 and dist[cur * 2] == -1:
        queue.appendleft(cur * 2)
        dist[cur * 2] = dist[cur]
    if cur > 0 and dist[cur - 1] == -1:
        queue.append(cur - 1)
        dist[cur - 1] = dist[cur] + 1
    if cur + 1 <= 100000 and dist[cur + 1] == -1:
        queue.append(cur + 1)
        dist[cur + 1] = dist[cur] + 1

print(dist[K])