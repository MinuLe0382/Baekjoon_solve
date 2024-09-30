import sys
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n + 1)]
p = [[] for _ in range(n + 1)]
for i in range(1, n):
    a, b = map(int, input().rstrip().split())
    adj[a].append(b)
    adj[b].append(a)

stack = [1]
visited = set()
visited.add(1)
while stack:
    cur = stack.pop()
    for nxt in adj[cur]:
        if nxt not in visited:
            stack.append(nxt)
            visited.add(nxt)
            p[nxt].append(cur)

for i in range(2, n + 1):
    print(*p[i])