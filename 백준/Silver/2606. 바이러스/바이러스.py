# adj_list & DFS

num = int(input())
connection = int(input())
adj = [[] for _ in range(num + 1)]
for _ in range(connection):
    start, end = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)

stack = [1]
visited = set()
visited.add(1) # 1 0 하면 -1이 나오지 않게 해야함
while stack:
    cur = stack.pop()
    for nxt in adj[cur]:
        if nxt not in visited:
            visited.add(nxt)
            stack.append(nxt)

print(len(visited) - 1)