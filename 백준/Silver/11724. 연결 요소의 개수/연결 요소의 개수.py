from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

adj_lst = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    adj_lst[s].append(e)
    adj_lst[e].append(s)

visited1 = set()
queue = deque()
cnt = 0

for i in range(1, N + 1):
    if i in visited1:
        continue
    else:
        visited1.add(i)
        queue.append(i)
        cnt += 1
        
    while queue:
        current = queue.popleft()
        for nxt in adj_lst[current]: # 정점번호가 직접 담겨있다.
            if nxt in visited1:
                continue

            visited1.add(nxt)
            queue.append(nxt)

print(cnt)