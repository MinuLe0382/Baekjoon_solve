import sys
input = sys.stdin.readline

def find(x): # 루트를 찾아가는 경로의 모든 노드를 바로 루트에 붙여버린다.
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_root, y_root = find(x), find(y)
    if rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    elif rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    else:
        parent[x_root] = y_root
        rank[y_root] += 1
        
N, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b, w = map(int, input().split())
    edges.append((w, a, b)) # 가중치를 앞에두면 정렬할때 편리하다.

edges.sort() # 가중치순 정렬
parent = [i for i in range(N + 1)]
rank = [0] * (N + 1)
cnt = 0 # 뽑은 간선 개수
ans = 0 # 가중치 누적값을 더해줄 변수
for w, a, b in edges: # 하나씩 간선 뽑기
    if find(a) != find(b):
        union(a, b)
        cnt += 1
        ans += w
        
    if cnt == N - 1:
        ans -= w
        break
        
print(ans)