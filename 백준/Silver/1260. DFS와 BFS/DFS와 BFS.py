import sys
input = sys.stdin.readline
from collections import deque

N, M, V = map(int, input().rstrip().split())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end = map(int, input().rstrip().split())
    if end not in adj[start]:
        adj[start].append(end)
    if start not in adj[end]:    
        adj[end].append(start)

# BFS (queue)
queue = deque([V])
visitlist2 = []
while queue:
    cur = queue.popleft()
    if cur not in visitlist2:
        visitlist2.append(cur)
    adj[cur].sort()
    for nxt in adj[cur]:
        if nxt not in visitlist2:
            queue.append(nxt)

# DFS (stack)
stack = [V]
visitlist1 = []
while stack:
    cur = stack.pop()
    if cur not in visitlist1:
        visitlist1.append(cur)
    adj[cur].sort(reverse = True) # 반대로 정렬해야 작은 노드부터 꺼낸다.
    for nxt in adj[cur]:
        if nxt not in visitlist1:
            stack.append(nxt)

print(*visitlist1)
print(*visitlist2)