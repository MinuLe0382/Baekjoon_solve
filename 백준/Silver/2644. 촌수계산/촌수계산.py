import sys
input = sys.stdin.readline
from collections import deque

flag = False
person = int(input())
target1, target2 = map(int, input().rstrip().split())
m = int(input())
adj = [[] for _ in range(person + 1)]
for _ in range(m):
    x, y = map(int, input().rstrip().split())
    adj[x].append(y)
    adj[y].append(x)

visited = set()
queue = deque([[target1, 0]])
while queue:
    cur, curdist = queue.popleft()
    if cur == target2:
        flag = True
        print(curdist)
        break
    if cur not in visited:
        visited.add(cur)
    for nxt in adj[cur]:
        if nxt not in visited:
            queue.append([nxt, curdist + 1])

if flag == False:
    print(-1)