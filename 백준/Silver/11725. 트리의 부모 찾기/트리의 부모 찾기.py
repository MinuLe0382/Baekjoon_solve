import sys
sys.setrecursionlimit(10000000)

N = int(input()) # 간선의 갯수는 n - 1개로 확정이 된다.
tree = [[] for _ in range(N + 1)]

def DFS(cur, parent):
    # 방문
    result[cur] = parent
    visited.add(cur)
    for nxt in tree[cur]:
        if nxt not in visited:
            DFS(nxt, cur) # 어디를 타고 넘어왔는지의 정보를 가지고 간다.
    # 탐색
for i in range(N - 1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

visited = set()
result = [0] * (N + 1)
DFS(1, -1) # 1의 부모는 아무도 관심이 없다.
for i in range(2, len(result)):
    print(result[i])